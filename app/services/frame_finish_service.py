from flask import jsonify

from app import db
from app.models.frame_finish import FrameFinish
from app.repositories.frame_finish_repository import get_all_ffs_db, get_ff_by_id, get_ff_by_type, delete_ff_by_id


def create_ff(data):
    type_ = data.get('type', None)
    price = data.get('price', 0)
    stock = data.get('stock', 0)
    in_stock = False

    if stock > 0:
        in_stock = True

    if not type_:
        return jsonify({"message": "Please provide type of frame finish"}), 422

    existing_ff = get_ff_by_type(type_)

    if existing_ff:
        return jsonify({"message": "The frame finish type already exists."}), 422

    new_ft = FrameFinish(type=type_, price=price, in_stock=in_stock, stock=stock)
    db.session.add(new_ft)
    db.session.commit()

    return jsonify({"message": "Frame finish created successfully"}), 201


def delete_ff(id):
    delete_ff_by_id(id)
    return jsonify({"message": "Frame finish deleted successfully"}), 204


def update_ff(id, data):
    type_ = data.get('type', None)
    price = data.get('price', 0)
    stock = data.get('stock', 0)
    in_stock = False

    if stock > 0:
        in_stock = True

    if not type_:
        return jsonify({"message": "Please provide type of frame finish"}), 422

    existing_ff = get_ff_by_id(id)

    if not existing_ff:
        return jsonify({"message": "Please provide existing frame type finish"}), 422

    if existing_ff.type != type_:
        existing_ff_with_type = get_ff_by_type(type_)
        if existing_ff_with_type:
            return jsonify({"message": "The frame finish type already exists"}), 422
        existing_ff.type = type_

    existing_ff.price = price
    existing_ff.stock = stock
    existing_ff.in_stock = in_stock

    db.session.add(existing_ff)
    db.session.commit()

    return jsonify({"message": "Frame Finish Type updated successfully"}), 200


def get_ff(id):
    ff = get_ff_by_id(id)
    return jsonify({
        "data": ff.to_dict()}
    ), 200


def get_all_ffs():
    ffs = get_all_ffs_db()
    return jsonify({
        "data": [ff.to_dict() for ff in ffs]}
    ), 200
