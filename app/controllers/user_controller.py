from flask import Blueprint, jsonify
from flask_jwt_extended import jwt_required, get_jwt_identity
from flask_login import login_required, current_user
from app.models.user import User

bp = Blueprint("user", __name__)


@bp.route("/profile", methods=["GET"])
@login_required
def profile():
    return jsonify(current_user.to_dict()), 200


@bp.route("/me", methods=["GET"])
@jwt_required()
def me():
    user_id = get_jwt_identity()
    user = User.query.get(user_id)
    return jsonify(user.to_dict()) if user else (jsonify({"message": "User not found"}), 404)
