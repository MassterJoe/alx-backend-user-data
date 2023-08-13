#!/usr/bin/env python3
""" Create a class SessionAuth that inherits from Auth
"""
from api.v1.auth.auth import Auth
import uuid
from models.user import User


class SessionAuth(Auth):
    """A class SessionAuth that inherits from Auth
    """

    user_id_by_session_id = {}

    def create_session(self, user_id: str = None) -> str:
        """ Session ID for a user_id
        """

        if user_id is None or type(user_id) is not str:
            return None
        else:
            session_id = str(uuid.uuid4())
            self.user_id_by_session_id[session_id] = user_id
            return session_id

    def user_id_for_session_id(self, session_id: str = None) -> str:
        """It returns a User ID based on a Session ID"""
        if session_id is None or type(session_id) is not str:
            return None
        else:
            user_id = str(uuid.uuid4())
            val = self.user_id_by_session_id.get(session_id)
            self.user_id_by_session_id[user_id] = val
            return self.user_id_by_session_id[user_id]

    def current_user(self, request=None):
        """ It returns a User instance based on a cookie value"""
        session_cokie = self.session_cookie(request)
        user_id = self.user_id_for_session_id(session_cokie)
        return User.get(user_id)

    def destroy_session(self, request=None):
        """ deletes the user session / logout:"""
        if request is None:
            return False
        session_id_cookie = self.session_cookie(request)
        if not session_id_cookie:
            return False
        user_id = self.user_id_for_session_id(session_id_cookie)
        if not user_id:
            return False
        del self.user_id_by_session_id[session_id_cookie]
        return True
