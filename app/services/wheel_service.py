from flask import jsonify

from app import db
from app.models.wheel import Wheel
from app.repositories.wheel_repository import get_wheel_by_type, get_wheel_by_id, delete_wheel_by_id, get_all_wheels_db


def create_wheel(data):
    type_wheel = data.get('type', None)
    price = data.get('price', 0)
    stock = data.get('stock', 0)
    in_stock = False

    if stock > 0:
        in_stock = True

    if not type_wheel:
        return jsonify({"message": "Please provide type of wheel"}), 422

    existing_wheel = get_wheel_by_type(type_wheel)

    if existing_wheel:
        return jsonify({"message": "The wheel with the provided type already exist."}), 422

    new_wheel = Wheel(type=type_wheel, price=price, in_stock=in_stock, stock=stock)
    db.session.add(new_wheel)
    db.session.commit()

    return jsonify({"message": "Wheel created successfully"}), 201


def delete_wheel(id):
    delete_wheel_by_id(id)
    return jsonify({"message": "Wheel deleted successfully"}), 204


def update_wheel(id, data):
    type_wheel = data.get('type', None)
    price = data.get('price', 0)
    stock = data.get('stock', 0)
    in_stock = False

    if stock > 0:
        in_stock = True

    if not type_wheel:
        return jsonify({"message": "Please provide type of wheel"}), 422

    existing_wheel = get_wheel_by_id(id)

    if not existing_wheel:
        return jsonify({"message": "Please provide existing wheel"}), 422

    if existing_wheel.type != type_wheel:
        existing_wheel_with_type = get_wheel_by_type(type_wheel)
        if existing_wheel_with_type:
            return jsonify({"message": "The wheel with the provided type already exist."}), 422
        existing_wheel.type = type_wheel

    existing_wheel.price = price
    existing_wheel.stock = stock
    existing_wheel.in_stock = in_stock

    db.session.add(existing_wheel)
    db.session.commit()

    return jsonify({"message": "Wheel updated successfully"}), 200


def get_wheel(id):
    wheel = get_wheel_by_id(id)
    return jsonify({
        "data": wheel.to_dict()}
    ), 200


def get_all_wheels():
    wheels = get_all_wheels_db()
    return jsonify({
        "data": [wheel.to_dict() for wheel in wheels]}
    ), 200
