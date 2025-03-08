from flask import Blueprint, request
from flask_login import login_required

from app.services.valid_combinations_service import get_all_vcs, delete_vc, create_vc
from app.utils.decorators import admin_required

bp = Blueprint("valid-combinations", __name__)


@bp.route("/create", methods=["POST"])
@login_required
@admin_required
def create():
    data = request.json
    response = create_vc(data)
    return response


@bp.route("/delete/<int:id>", methods=["DELETE"])
@login_required
@admin_required
def delete(id):
    response = delete_vc(id)
    return response


@bp.route("/", methods=["GET"])
@login_required
@admin_required
def get_all():
    response = get_all_vcs()
    return response