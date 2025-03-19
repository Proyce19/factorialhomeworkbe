from flask import Blueprint, request
from flask_jwt_extended import jwt_required
from flask_login import login_required

from app.services.bike_service import get_all_bikes, get_bike, delete_bike, create_bike, update_bike

bp = Blueprint("bike", __name__)


@bp.route("/create", methods=["POST"])
@login_required
@jwt_required()
def create():
    data = request.json
    response = create_bike(data)
    return response


@bp.route("/delete/<int:id>", methods=["DELETE"])
@login_required
@jwt_required()
def delete(id):
    response = delete_bike(id)
    return response


@bp.route("/update/<int:id>", methods=["PUT"])
@login_required
@jwt_required()
def update(id):
    data = request.json
    response = update_bike(id,data)
    return response


@bp.route("/get/<int:id>", methods=["GET"])
@login_required
@jwt_required()
def get(id):
    response = get_bike(id)
    return response


@bp.route("/", methods=["GET"])
@login_required
@jwt_required()
def get_all():
    response = get_all_bikes()
    return response
