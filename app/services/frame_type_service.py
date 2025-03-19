from flask import jsonify

from app import db
from app.models.frame_type import FrameType
from app.repositories.frame_type_repository import delete_ft_by_id, get_ft_by_type, get_ft_by_id, get_all_fts_db


def create_ft(data):
    type_ = data.get('type', None)
    price = data.get('price', 0)
    stock = data.get('stock', 0)
    in_stock = False

    if stock > 0:
        in_stock = True

    if not type_:
        return jsonify({"message": "Please provide type of frame"}), 422

    existing_ft = get_ft_by_type(type_)

    if existing_ft:
        return jsonify({"message": "The frame with the provided type already exist."}), 422

    new_ft = FrameType(type=type_, price=price, in_stock=in_stock, stock=stock)
    db.session.add(new_ft)
    db.session.commit()

    return jsonify({"message": "Frame type created successfully"}), 201


def delete_ft(id):
    delete_ft_by_id(id)
    return jsonify({"message": "Frame type deleted successfully"}), 204


def update_ft(id, data):
    type_ = data.get('type', None)
    price = data.get('price', 0)
    stock = data.get('stock', 0)
    in_stock = False

    if stock > 0:
        in_stock = True

    if not type_:
        return jsonify({"message": "Please provide type of frame"}), 422

    existing_ft = get_ft_by_id(id)

    if not existing_ft:
        return jsonify({"message": "Please provide existing frame type"}), 422

    if existing_ft.type != type_:
        existing_ft_with_type = get_ft_by_type(type_)
        if existing_ft_with_type:
            return jsonify({"message": "The frame with the provided type already exist."}), 422
        existing_ft.type = type_

    existing_ft.price = price
    existing_ft.stock = stock
    existing_ft.in_stock = in_stock

    db.session.add(existing_ft)
    db.session.commit()

    return jsonify({"message": "Frame Type updated successfully"}), 200


def get_ft(id):
    ft = get_ft_by_id(id)
    return jsonify({
        "data": ft.to_dict()}
    ), 200



def get_all_fts():
    fts = get_all_fts_db()
    return jsonify({
        "data": [ft.to_dict() for ft in fts]}
    ), 200
