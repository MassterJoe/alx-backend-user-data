#!/usr/bin/env python3
"""Create Auth class
a class to manage the API authentication."""
from flask import request
from typing import List, TypeVar


class Auth:
    """Create Auth class
    a class to manage the API authentication."""
    def require_auth(self, path: str, excluded_paths: List[str]) -> bool:
        """public method require_auth"""

        if excluded_paths is None or excluded_paths == [] or path is None:
            return True

        for i in excluded_paths:
            if i == path+'/' or i == path or path in excluded_paths:
                return False
            elif i.endswith('*'):
                if path == i[:2]:
                    return False
            return True

    def authorization_header(self, request=None) -> str:
        """ public method authorization_header """

        if request is None:
            return None
        val = request.headers.get("Authorization")
        if val is None:
            return None
        return val

    def current_user(self, request=None) -> TypeVar('User'):
        """ public method current_user """
        return None
