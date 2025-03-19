from flask import jsonify

from app import db
from app.models.product_type import ProductType
from app.repositories.product_repository import get_products_by_type_id
from app.repositories.product_type_repository import get_pt_by_type, delete_pt_by_id, get_pt_by_id, get_all_pts_db


def create_pt(data):
    type_ = data.get('type', None)

    if not type_:
        return jsonify({"message": "Please provide type of product"}), 422

    existing_pt = get_pt_by_type(type_)

    if existing_pt:
        return jsonify({"message": "The product type already exist."}), 422

    new_pt = ProductType(type=type_)
    db.session.add(new_pt)
    db.session.commit()

    return jsonify({"message": "Product type created successfully"}), 201


def delete_pt(id):
    products = get_products_by_type_id(id)
    if products and len(products) > 0:
        jsonify({"message": "Product type cannot be deleted"}), 422
    delete_pt_by_id(id)
    db.session.commit()
    return jsonify({"message": "Product type deleted successfully"}), 204


def update_pt(id, data):
    type_ = data.get('type', None)

    if not type_:
        return jsonify({"message": "Please provide type of product"}), 422

    existing_pt = get_pt_by_id(id)

    if not existing_pt:
        return jsonify({"message": "Please provide existing type product"}), 422

    if existing_pt.type != type_:
        existing_pt_with_type = get_pt_by_type(type_)
        if existing_pt_with_type:
            return jsonify({"message": "The product type already exist."}), 422
        existing_pt.type = type_

    db.session.add(existing_pt)
    db.session.commit()

    return jsonify({"message": "Product Type updated successfully"}), 200


def get_pt(id):
    pt = get_pt_by_id(id)

    if pt:
        data = pt.to_dict()
    else:
        data = {}

    return jsonify({
        "data": data}
    ), 200


def get_all_pts():
    pts = get_all_pts_db()

    if pts:
        if len(pts):
            data = [pt.to_dict() for pt in pts]
        else:
            data = []
    else:
        data = []

    return jsonify({
        "data": data}
    ), 200
