#!/usr/bin/env python3
"""Create Auth class
a class to manage the API authentication."""
from flask import request
from typing import List, TypeVar
import os


class Auth:
    """Create Auth class
    a class to manage the API authentication."""
    def require_auth(self, path: str, excluded_paths: List[str]) -> bool:
        """public method require_auth"""

        if path is None:
            return True
        elif excluded_paths is None or excluded_paths == []:
            return True
        elif path in excluded_paths:
            return False
        else:
            for i in excluded_paths:
                if i.startswith(path):
                    return False
                if path.startswith(i):
                    return False
                if i[-1] == "*":
                    if path.startswith(i[:-1]):
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

    def session_cookie(self, request=None) -> str:
        """It returns a cookie value from a request
        """
        if request is None:
            return None
        cookie_session = os.environ.get('SESSION_NAME', '_my_session_id')
        val = request.cookies.get(cookie_session)
        return val
