from typing import Tuple

from flask import jsonify, Response
from flask_jwt_extended import create_access_token
from flask_login import login_user, logout_user
from werkzeug.security import check_password_hash, generate_password_hash

from app import db
from app.models.user import User
from app.repositories.user_repository import get_user_by_username


def login_fct_user(data: dict) -> tuple[Response, int]:
    username = data.get("username")
    password = data.get("password")

    user = get_user_by_username(username)

    if not user or not check_password_hash(user.password_hash, password):
        return jsonify({"message": "Invalid credentials"}), 401

    login_user(user)
    access_token = create_access_token(identity=user.id)
    return jsonify({"message": "Logged in", "access_token": access_token}), 200


def register_fct_user(data: dict) -> tuple[Response, int]:
    username = data.get("username")
    password = data.get("password")

    if get_user_by_username(username):
        return jsonify({"message": "User already exists"}), 400

    hashed_password = generate_password_hash(password, method='pbkdf2')
    new_user = User(username=username, password_hash=hashed_password)
    db.session.add(new_user)
    db.session.commit()

    return jsonify({"message": "User registered successfully"}), 201


def logout_fct_user():
    logout_user()
    return jsonify({"message": "Logged out"}), 200
