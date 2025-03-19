from flask import Blueprint, request
from flask_login import login_required

from app.services.chain_service import create_chain, delete_chain, update_chain, get_chain, get_all_chains
from app.utils.decorators import admin_required

bp = Blueprint("chain", __name__)


@bp.route("/create", methods=["POST"])
@login_required
@admin_required
def create():
    data = request.json
    response = create_chain(data)
    return response


@bp.route("/delete/<int:id>", methods=["DELETE"])
@login_required
@admin_required
def delete(id):
    response = delete_chain(id)
    return response


@bp.route("/update/<int:id>", methods=["PUT"])
@login_required
@admin_required
def update(id):
    data = request.json
    response = update_chain(id, data)
    return response


@bp.route("/get/<int:id>", methods=["GET"])
@login_required
@admin_required
def get(id):
    response = get_chain(id)
    return response



@bp.route("/", methods=["GET"])
@login_required
def get_all():
    response = get_all_chains()
    return response
