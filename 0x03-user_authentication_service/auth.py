#!/usr/bin/env python3
"""
 method that takes in a password string
arguments and returns bytes.
"""
import bcrypt
from db import DB
from user import User
from sqlalchemy.orm.exc import NoResultFound
import uuid
from typing import Union


def _hash_password(password: str) -> bytes:
    """_hash_password method
    returns bytes"""
    password = bytes(password, 'utf-8')
    salt = bcrypt.gensalt()
    hashed_password = bcrypt.hashpw(password, salt)
    return hashed_password


def _generate_uuid() -> str:
    """return a string representation of a new UUID
    """
    new_uuid = uuid.uuid4()
    return str(new_uuid)


class Auth:
    """Auth class to interact with the authentication database.
    """

    def __init__(self):
        self._db = DB()

    def register_user(self, email: str, password: str) -> User:
        """ Auth.register_user should take mandatory email and
        password string arguments and return a User object.
        """
        try:
            self._db.find_user_by(email=email)
        except NoResultFound:
            hashed_password = _hash_password(password)
            new_user = self._db.add_user(email, hashed_password)
            return new_user
        raise ValueError('User {} already exists'.format(email))

    def valid_login(self, email: str, password: str) -> bool:
        """ expect email and password required arguments
        and return a boolean."""
        try:
            user = self._db.find_user_by(email=email)
            hashed_password = user.hashed_password
            if bcrypt.checkpw(password.encode('utf-8'), hashed_password):
                return True
            else:
                return False
        except NoResultFound:
            return False

    def create_session(self, email: str) -> Union[None, str]:
        """It finds the user corresponding to the email
        takes an email string argument
        returns the session ID as a string
        """
        try:
            user = self._db.find_user_by(email=email)
            session_id = _generate_uuid()
            self._db.update_user(user.id, session_id=session_id)
            return session_id
        except NoResultFound:
            return None

    def get_user_from_session_id(self, session_id: str) -> Union[str, None]:
        """  It takes a single session_id string argument
        returns the corresponding User or None.
        """
        if session_id is None:
            return None
        try:
            user = self._db.find_user_by(session_id=session_id)
        except NoResultFound:
            return None
        return user

    def destroy_session(self, user_id: int) -> None:
        """ The method takes a single user_id integer
        argument and returns None."""
        if user_id is None:
            return None
        return self._id.update_user(user_id, session_id=None)
