from flask import Blueprint, request
from flask_login import login_required

from app.extensions import login_manager
from app.repositories.user_repository import get_user_by_id
from app.services.auth_service import login_fct_user, register_fct_user, logout_fct_user

bp = Blueprint("auth", __name__)


@login_manager.user_loader
def load_user(user_id):
    user = get_user_by_id(int(user_id))
    return user


@bp.route("/register", methods=["POST"])
def register():
    data = request.json
    response = register_fct_user(data)
    return response


@bp.route("/login", methods=["POST", 'OPTIONS'])
def login():
    data = request.json
    response = login_fct_user(data)
    return response


@bp.route("/logout", methods=["POST"])
@login_required
def logout():
    response = logout_fct_user()
    return response
