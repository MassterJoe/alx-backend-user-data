#!/usr/bin/env python3
"""
 method that takes in a password string
arguments and returns bytes.
"""
import bcrypt


def _hash_password(password: str) -> bytes:
    """_hash_password method
    returns bytes"""
    password = bytes(password, 'utf-8')
    salt = bcrypt.gensalt()
    hashed_password = bcrypt.hashpw(password, salt)
    return hashed_password
