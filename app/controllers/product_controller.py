from flask import Blueprint, request
from flask_login import login_required

from app.services.product_service import create_product, get_product, get_all_products, update_product, delete_product
from app.utils.decorators import admin_required

bp = Blueprint("product", __name__)


@bp.route("/create", methods=["POST"])
@login_required
@admin_required
def create():
    data = request.json
    response = create_product(data)
    return response


@bp.route("/delete/<int:id>", methods=["DELETE"])
@login_required
@admin_required
def delete(id):
    response = delete_product(id)
    return response


@bp.route("/update/<int:id>", methods=["PUT"])
@login_required
@admin_required
def update(id):
    data = request.json
    response = update_product(id, data)
    return response


@bp.route("/get/<int:id>", methods=["GET"])
@login_required
def get(id):
    response = get_product(id)
    return response



@bp.route("/", methods=["GET"])
@login_required
def get_all():
    response = get_all_products()
    return response
