from flask import Blueprint, request
from flask_login import login_required

from app.services.frame_service import create_frame, delete_frame, update_frame, get_frame, get_all_frames
from app.utils.decorators import admin_required

bp = Blueprint("frame", __name__)


@bp.route("/create", methods=["POST"])
@login_required
@admin_required
def create():
    data = request.json
    response = create_frame(data)
    return response


@bp.route("/delete/<int:id>", methods=["DELETE"])
@login_required
@admin_required
def delete(id):
    response = delete_frame(id)
    return response


@bp.route("/update/<int:id>", methods=["PUT"])
@login_required
@admin_required
def update(id):
    response = update_frame(id)
    return response


@bp.route("/get/<int:id>", methods=["GET"])
@login_required
@admin_required
def get(id):
    response = get_frame(id)
    return response


@bp.route("/", methods=["GET"])
@login_required
def get_all():
    response = get_all_frames()
    return response
