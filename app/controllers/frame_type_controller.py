from flask import Blueprint, request
from flask_login import login_required

from app.services.frame_type_service import get_ft, update_ft, delete_ft, create_ft, get_all_fts
from app.utils.decorators import admin_required

bp = Blueprint("frame-type", __name__)


@bp.route("/create", methods=["POST"])
@login_required
@admin_required
def create():
    data = request.json
    response = create_ft(data)
    return response


@bp.route("/delete/<int:id>", methods=["DELETE"])
@login_required
@admin_required
def delete(id):
    response = delete_ft(id)
    return response


@bp.route("/update/<int:id>", methods=["PUT"])
@login_required
@admin_required
def update(id):
    response = update_ft(id)
    return response


@bp.route("/get/<int:id>", methods=["GET"])
@login_required
@admin_required
def get(id):
    response = get_ft(id)
    return response



@bp.route("/", methods=["GET"])
@login_required
def get_all():
    response = get_all_fts()
    return response
