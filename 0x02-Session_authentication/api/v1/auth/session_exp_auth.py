#!/usr/bin/env python3
"""Create a class SessionExpAuth that inherits from SessionAuth
"""
from api.v1.auth.session_auth import SessionAuth
import os
from datetime import datetime, timedelta


class SessionExpAuth(SessionAuth):
    """ Class SessionExpAuth inherits from SessionAuth"""
    def __init__(self):

        session_env = os.getenv('SESSION_DURATION')
        try:
            self.session_duration = int(session_env)
        except ValueError:
            self.session_duration = 0

    def create_session(self, user_id=None):
        """ create_session method """
        try:
            session_id = super().create_session(user_id)
        except Exception:
            return None
        self.user_id_by_session_id['session_id'] = {
            'user_id': user_id,
            'created_at': datetime.now()
        }
        return session_id

    def user_id_for_session_id(self, session_id=None):
        """ Overloading  user_id_for_session_id"""
        if session_id is None:
            return None
        elif session_id not in self.user_id_by_session_id[session_id]:
            return None
        elif 'created_at' not in self.user_id_by_session_id[session_id]:
            return None
        elif self.session_duration <= 0:
            return self.user_id_by_session_id[session_id].get('user_id')
        created_at = self.user_id_by_session_id[session_id].get('created_at')
        total_time = created_at + timedelta(seconds=self.session_duration)
        if total_time < datetime.now():
            return None
        return self.user_id_by_session_id[session_id].get('user_id')
