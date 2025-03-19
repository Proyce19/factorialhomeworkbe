from flask import Blueprint, request
from flask_login import login_required

from app.services.wheel_service import create_wheel, delete_wheel, update_wheel, get_wheel, get_all_wheels
from app.utils.decorators import admin_required

bp = Blueprint("wheel", __name__)


@bp.route("/create", methods=["POST"])
@login_required
@admin_required
def create():
    data = request.json
    response = create_wheel(data)
    return response


@bp.route("/delete/<int:id>", methods=["DELETE"])
@login_required
@admin_required
def delete(id):
    response = delete_wheel(id)
    return response


@bp.route("/update/<int:id>", methods=["PUT"])
@login_required
@admin_required
def update(id):
    data = request.json
    response = update_wheel(id, data)
    return response


@bp.route("/get/<int:id>", methods=["GET"])
@login_required
@admin_required
def get(id):
    response = get_wheel(id)
    return response


@bp.route("/", methods=["GET"])
@login_required
def get_all():
    response = get_all_wheels()
    return response
