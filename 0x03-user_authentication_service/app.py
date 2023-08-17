#!/usr/bin/env python3
"""
Create a Flask app that has a
single GET route ("/")
"""
from flask import Flask, jsonify, request, abort
from auth import Auth


app = Flask(__name__)
AUTH = Auth()


@app.route('/', methods=['GET'])
def hello_world():
    return jsonify({"message": "Bienvenue"})


@app.route('/users', methods=['POST'])
def users():
    """users endpoint
    """
    email = request.form.get('email')
    password = request.form.get('password')
    try:
        user = AUTH.register_user(email, password)
        return jsonify(
                    {"email": user.email,
                     "message": "user created"})
    except ValueError:
        return jsonify({"message": "email already registered"}), 400


@app.route('/sessions', methods=['POST'], strict_slashes=False)
def login() -> str:
    """ login"""
    email = request.form.get('email')
    password = request.form.get('password')

    if not AUTH.valid_login(email, password):
        abort(401)
    session_id = AUTH.create_session(email)
    response = jsonify(
                        {"email": f'{email}',
                         "message": "logged in"}
    )
    response.set_cookie("session_id", session_id)
    return response


@app.route('/sessions', methods=['DELETE'], strict_slashes=False)
def logout() -> str:
    """ logout """
    session_id = request.cookies.get('session_id')
    user = AUTH.get_user_from_session_id(session_id)
    if user:
        AUTH.destroy_session(user.id)
        response = jsonify({'message': 'logout successful'})
        response.delete_cookie('session_id')
        return redirect('/', code=302)
    else:
        abort(403)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port="5000")
