#!/usr/bin/env python3
"""
Create a class BasicAuth that inherits from Auth
"""
from api.v1.auth.auth import Auth
import base64


class BasicAuth(Auth):
    """Create a class BasicAuth that inherits from Auth"""

    def extract_base64_authorization_header(self,
                                            authorization_header: str) -> str:
        """ returns the Base64 part of the Authorization header
        for a Basic Authentication:"""

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
