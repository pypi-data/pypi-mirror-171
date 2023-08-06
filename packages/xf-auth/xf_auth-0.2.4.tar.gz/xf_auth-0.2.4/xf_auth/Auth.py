from datetime import datetime
from functools import update_wrapper
from typing import Type

from cryptography.fernet import Fernet
from flask import Response, request, session

from xf_auth.HTTPStatus import UNAUTHORIZED, SESSION_EXPIRED, FORBIDDEN, NOT_ACCEPTABLE
from xf_auth.Util import decode, included, encode


class Auth:
	secret_password: bytes = None
	class_name: Type[object] = None
	user_keys: list = None

	@staticmethod
	def set_password():
		Auth.secret_password = Fernet.generate_key()

	@staticmethod
	def set_user_origin(class_name: Type[object]) -> None:
		Auth.class_name = class_name

	@staticmethod
	def set_user_keys(keys: list) -> None:
		Auth.user_keys = keys
		if Auth.class_name is not None:
			aux = Auth.class_name()
			for key in keys:
				try:
					aux.__getattribute__(key)
				except AttributeError as exception:
					message = f"{key} not in {Auth.class_name} attributes"
					raise Exception(message) from exception

	@staticmethod
	def requires_token(operation):
		def verify_auth(*args, **kwargs):
			token = request.headers.get("Token")
			saved_token = None
			try:
				saved_token = session["token"]
				response = Response(status=UNAUTHORIZED)
				if token is not None and saved_token is not None and token == saved_token:
					session.modified = True
					response = operation(*args, **kwargs)
			except KeyError:
				response = Response(status=UNAUTHORIZED)
				if token is not None and saved_token is None:
					response = Response(status=SESSION_EXPIRED)
			return response

		return update_wrapper(verify_auth, operation)

	@staticmethod
	def requires_role(role: str):
		def decorator(operation):
			def verify_role(*args, **kwargs):
				token = request.headers.get("Token")
				response = Response(status=FORBIDDEN)
				if token is not None:
					values = Auth.decode_token(token)
					response = Response(status=FORBIDDEN)
					if str(values["is_owner"]) == str(role):
						response = operation(*args, **kwargs)
				return response

			return update_wrapper(verify_role, operation)

		return decorator

	@staticmethod
	def requires_payload(required_fields: set):
		def decorator(operation):
			def verify_payload(*args, **kwargs):
				if not included(required_fields, request.json):
					response = Response(status=NOT_ACCEPTABLE)
				else:
					response = operation(*args, **kwargs)
				return response

			return update_wrapper(verify_payload, operation)

		return decorator

	@staticmethod
	def generate_token(user) -> str or None:
		response: str or None = None
		if isinstance(user, Auth.class_name):
			if Auth.secret_password is None:
				Auth.set_password()
			timestamp = datetime.now().strftime("%H:%M:%S")

			value: str = ""
			for key in Auth.user_keys:
				value += user.__getattribute__(key) + "/"

			value += timestamp
			response = encode(value, Auth.secret_password)
		return response

	@staticmethod
	def decode_token(token: str) -> dict:
		decoded_token = decode(token, Auth.secret_password)
		decoded_token = decoded_token.split("/")
		return {
			"email": decoded_token[0],
			"password": decoded_token[1]
		}
