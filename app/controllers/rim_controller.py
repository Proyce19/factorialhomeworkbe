from flask import Blueprint, request
from flask_login import login_required

from app.services.rim_service import create_rim, get_all_rims, get_rim, delete_rim, update_rim
from app.utils.decorators import admin_required

bp = Blueprint("rim", __name__)


@bp.route("/create", methods=["POST"])
@login_required
@admin_required
def create():
    data = request.json
    response = create_rim(data)
    return response


@bp.route("/delete/<int:id>", methods=["DELETE"])
@login_required
@admin_required
def delete(id):
    response = delete_rim(id)
    return response


@bp.route("/update/<int:id>", methods=["PUT"])
@login_required
@admin_required
def update(id):
    response = update_rim(id)
    return response


@bp.route("/get/<int:id>", methods=["GET"])
@login_required
@admin_required
def get(id):
    response = get_rim(id)
    return response



@bp.route("/", methods=["GET"])
@login_required
def get_all():
    response = get_all_rims()
    return response
