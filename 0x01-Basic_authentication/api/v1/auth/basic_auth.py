#!/usr/bin/env python3
"""
Basic authentication module for the API.
"""
from api.v1.auth.auth import Auth
import base64
from typing import Tuple, TypeVar
from models.user import User


class BasicAuth(Auth):
    """
    Create a class BasicAuth that inherits from Auth.
    """

    def extract_base64_authorization_header(
            self,
            authorization_header: str) -> str:
        """Extracts the Base64 part of the Authorization header
        for a Basic Authentication.
        """

        if authorization_header is None:
            return None
        if type(authorization_header) is not str:
            return None

        header_beg = "Basic" + " "
        if authorization_header.startswith(header_beg):
            basic_part, base64_part = authorization_header.split(' ')
            return base64_part
        else:
            return None

    def decode_base64_authorization_header(
            self,
            base64_authorization_header: str) -> str:
        """Decodes value of a Base64 string
        base64_authorization_header."""

        if base64_authorization_header is None:
            return None
        if type(base64_authorization_header) is str:
            try:
                decoded_str = base64.b64decode(
                    base64_authorization_header).decode('utf-8')
                return decoded_str
            except base64.binascii.Error:
                return None
        else:
            return None

    def extract_user_credentials(
            self,
            decoded_base64_authorization_header: str) -> Tuple[str, str]:
        """It returns the user email and password
        from the Base64 decoded value."""
        if decoded_base64_authorization_header is None:
            return None, None
        if type(
            decoded_base64_authorization_header
        ) is str:
            if ':' in decoded_base64_authorization_header:
                email, pas = decoded_base64_authorization_header.split(':')
                return email, pas
            else:
                return None, None
        else:
            return None, None

    def user_object_from_credentials(
            self, user_email: str, user_pwd: str) -> TypeVar('User'):
        """It returns the User instance based on his email and password."""
        if [user_email, user_pwd] is None:
            return None
        if type(user_email) is str and type(user_pwd) is str:
            try:
                users = User.search({'email': user_email})
            except Exception:
                return None
            if (len(users) <= 0):
                return None
            if users[0].is_valid_password(user_pwd):
                return users[0]
            else:
                return None
        else:
            return None
