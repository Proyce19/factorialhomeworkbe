from functools import wraps
from flask import request, jsonify
from flask_jwt_extended import get_jwt_identity, jwt_required
from app.models.user import User


def admin_required(f):
    @wraps(f)
    @jwt_required()
    def decorated_function(*args, **kwargs):
        user_id = get_jwt_identity()
        user = User.query.get(user_id)

        if user is None or not user.is_admin:
            return jsonify({"message": "Access denied. Admins only."}), 403

        return f(*args, **kwargs)

    return decorated_function
