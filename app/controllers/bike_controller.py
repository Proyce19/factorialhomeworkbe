from flask import Blueprint, request
from flask_login import login_required

from app.services.chain_service import create_chain, delete_chain, update_chain, get_chain, get_all_chains
from app.utils.decorators import admin_required

bp = Blueprint("bike", __name__)


@bp.route("/create", methods=["POST"])
@login_required
@admin_required
def create():
    data = request.json
    response = create_bike(data)
    return response


@bp.route("/create-custom", methods=["POST"])
@login_required
def create():
    data = request.json
    response = create_custom_bike(data)
    return response


@bp.route("/delete/<int:id>", methods=["DELETE"])
@login_required
@admin_required
def delete(id):
    response = delete_bike(id)
    return response


@bp.route("/delete-custom/<int:id>", methods=["DELETE"])
@login_required
@admin_required
def delete(id):
    response = delete_custom_bike(id)
    return response


@bp.route("/update/<int:id>", methods=["PUT"])
@login_required
@admin_required
def update(id):
    response = update_bike(id)
    return response


@bp.route("/update-custom/<int:id>", methods=["PUT"])
@login_required
def update(id):
    response = update_custom_bike(id)
    return response


@bp.route("/get/<int:id>", methods=["GET"])
@login_required
def get(id):
    response = get_bike(id)
    return response


@bp.route("/", methods=["GET"])
@login_required
def get_all():
    response = get_all_bikes()
    return response
