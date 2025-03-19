from flask import Blueprint, request
from flask_login import login_required

from app.services.product_type_service import get_pt, get_all_pts, update_pt, delete_pt, create_pt
from app.utils.decorators import admin_required

bp = Blueprint("product-type", __name__)


@bp.route("/create", methods=["POST"])
@login_required
@admin_required
def create():
    data = request.json
    response = create_pt(data)
    return response


@bp.route("/delete/<int:id>", methods=["DELETE"])
@login_required
@admin_required
def delete(id):
    response = delete_pt(id)
    return response


@bp.route("/update/<int:id>", methods=["PUT"])
@login_required
@admin_required
def update(id):
    data = request.json
    response = update_pt(id, data)
    return response


@bp.route("/get/<int:id>", methods=["GET"])
@login_required
@admin_required
def get(id):
    response = get_pt(id)
    return response



@bp.route("/", methods=["GET"])
@login_required
def get_all():
    response = get_all_pts()
    return response
