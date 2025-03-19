from flask import Blueprint, request
from flask_jwt_extended import jwt_required
from flask_login import login_required

from app.services.cart_service import create_cart, delete_cart, update_cart, get_cart

bp = Blueprint("cart", __name__)


@bp.route("/create", methods=["POST"])
@login_required
@jwt_required()
def create():
    data = request.json
    response = create_cart(data)
    return response


@bp.route("/delete/<int:id>", methods=["DELETE"])
@login_required
def delete(id):
    response = delete_cart(id)
    return response


@bp.route("/update/<int:id>", methods=["PUT"])
@login_required
def update(id):
    data = request.json
    response = update_cart(id, data)
    return response


@bp.route("/get/<int:id>", methods=["GET"])
@login_required
def get(id):
    response = get_cart(id)
    return response

