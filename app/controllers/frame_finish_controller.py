from flask import Blueprint, request
from flask_login import login_required

from app.services.frame_finish_service import create_ff, delete_ff, update_ff, get_ff, get_all_ffs
from app.utils.decorators import admin_required

bp = Blueprint("frame-finish", __name__)


@bp.route("/create", methods=["POST"])
@login_required
@admin_required
def create():
    data = request.json
    response = create_ff(data)
    return response


@bp.route("/delete/<int:id>", methods=["DELETE"])
@login_required
@admin_required
def delete(id):
    response = delete_ff(id)
    return response


@bp.route("/update/<int:id>", methods=["PUT"])
@login_required
@admin_required
def update(id):
    response = update_ff(id)
    return response


@bp.route("/get/<int:id>", methods=["GET"])
@login_required
@admin_required
def get(id):
    response = get_ff(id)
    return response


@bp.route("/", methods=["GET"])
@login_required
def get_all():
    response = get_all_ffs()
    return response
