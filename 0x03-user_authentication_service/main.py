#!/usr/bin/env python3
"""
end-to-end Integration Test
"""
import requests


BASE_URL = 'http://localhost:5000'


def register_user(email: str, password: str) -> None:
    """Registration Test
    """
    response = requests.post(
        f'{BASE_URL}/users',
        json={'email': email, 'password': password})
    assert response.status_code == 201


def log_in_wrong_password(email: str, password: str) -> None:
    """login wrong password Test
    """
    response = requests.post(
        f'{BASE_URL}/sessions',
        json={'email': email, 'password': password})
    assert response.status_code == 401


def log_in(email: str, password: str) -> str:
    """login Test
    """
    response = requests.post(
        f'{BASE_URL}/sessions',
        json={'email': email, 'password': password})
    assert response.status_code == 200
    data = response.json()
    assert 'session_id' in data
    return data['session_id']


def profile_unlogged() -> None:
    """profile get Test
    """
    response = requests.get(f'{BASE_URL}/profile')
    assert response.status_code == 403


def profile_logged(session_id: str) -> None:
    """profile Logged test
    """
    headers = {'Cookie': f'session_id={session_id}'}
    response = requests.get(f'{BASE_URL}/profile', headers=headers)
    assert response.status_code == 200
    data = response.json()
    assert 'email' in data


def log_out(session_id: str) -> None:
    """logout Test
    """
    headers = {'Cookie': f'session_id={session_id}'}
    response = requests.delete(
        f'{BASE_URL}/sessions', headers=headers)
    assert response.status_code == 204


def reset_password_token(email: str) -> str:
    """Reset password Token test
    """
    response = requests.post(
        f'{BASE_URL}/reset_password', data={'email': email})
    assert response.status_code == 200
    data = response.json()
    assert 'email' in data and 'reset_token' in data
    return data['reset_token']


def update_password(
        email: str,
        reset_token: str, new_password: str) -> None:
    """Update paswword Test
    """
    response = requests.put(
        f'{BASE_URL}/reset_password',
        data={'email': email,
              'reset_token': reset_token,
              'new_password': new_password})
    assert response.status_code == 200
    data = response.json()
    assert 'email' in data and 'message'\
        in data and data['message'] == 'Password updated'


EMAIL = "guillaume@holberton.io"
PASSWD = "b4l0u"
NEW_PASSWD = "t4rt1fl3tt3"


if __name__ == "__main__":

    register_user(EMAIL, PASSWD)
    log_in_wrong_password(EMAIL, NEW_PASSWD)
    profile_unlogged()
    session_id = log_in(EMAIL, PASSWD)
    profile_logged(session_id)
    log_out(session_id)
    reset_token = reset_password_token(EMAIL)
    update_password(EMAIL, reset_token, NEW_PASSWD)
    log_in(EMAIL, NEW_PASSWD)
