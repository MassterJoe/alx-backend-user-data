#!/usr/bin/env python3
from flask import request
from typing import List, TypeVar


class Auth:
    """Create Auth class"""
    def require_auth(self, path: str, excluded_paths: List[str]) -> bool:
        """public method require_auth"""

        if excluded_paths is None or excluded_paths == [] or path is None:
            return True
        if path in excluded_paths:
            return False
        for i in excluded_paths:
            if i == path+'/':
                return False
            return True

    def authorization_header(self, request=None) -> str:
        """ public method authorization_header """
        return None

    def current_user(self, request=None) -> TypeVar('User'):
        """ public method current_user """
        return None
