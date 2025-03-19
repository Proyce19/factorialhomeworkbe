from flask import jsonify

from app import db
from app.models.rim import Rim
from app.repositories.rim_repository import get_all_rims_db, get_rim_by_id, get_rim_by_color, delete_rim_by_id


def create_rim(data):
    color = data.get('color', None)
    price = data.get('price', 0)
    stock = data.get('stock', 0)
    in_stock = False

    if stock > 0:
        in_stock = True

    if not color:
        return jsonify({"message": "Please provide color for the rim"}), 422

    existing_rim = get_rim_by_color(color)

    if existing_rim:
        return jsonify({"message": "The rim with the provided color already exist."}), 422

    new_rim = Rim(color=color, price=price, in_stock=in_stock, stock=stock)
    db.session.add(new_rim)
    db.session.commit()

    return jsonify({"message": "Rim created successfully"}), 201


def delete_rim(id):
    delete_rim_by_id(id)
    return jsonify({"message": "Rim deleted successfully"}), 204


def update_rim(id, data):
    color = data.get('color', None)
    price = data.get('price', 0)
    stock = data.get('stock', 0)
    in_stock = False

    if stock > 0:
        in_stock = True

    if not color:
        return jsonify({"message": "Please provide color for the rim"}), 422

    existing_rim = get_rim_by_id(id)

    if not existing_rim:
        return jsonify({"message": "Please provide existing rim"}), 422

    if existing_rim.color != color:
        existing_chain_with_color = get_rim_by_color(color)
        if existing_chain_with_color:
            return jsonify({"message": "The Rim with the provided color already exist."}), 422
        existing_rim.type = color

    existing_rim.price = price
    existing_rim.stock = stock
    existing_rim.in_stock = in_stock

    db.session.add(existing_rim)
    db.session.commit()

    return jsonify({"message": "Rim updated successfully"}), 200


def get_rim(id):
    rim = get_rim_by_id(id)
    return jsonify({
        "data": rim.to_dict()}
    ), 200


def get_all_rims():
    rims = get_all_rims_db()
    return jsonify({
        "data": [rim.to_dict() for rim in rims]}
    ), 200
