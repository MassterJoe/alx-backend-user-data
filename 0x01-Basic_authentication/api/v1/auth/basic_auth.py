#!/usr/bin/env python3
"""
Basic authentication module for the API.
"""
from api.v1.auth.auth import Auth
import base64
from typing import Tuple


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
            return None
        if type(
            decoded_base64_authorization_header
        ) is str and ':' in decoded_base64_authorization_header:
            email, password = decoded_base64_authorization_header.split(':')
            return email, password
        else:
            return None
