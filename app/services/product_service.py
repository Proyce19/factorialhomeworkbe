from flask import jsonify

from app import db
from app.models.product import Product
from app.repositories.product_repository import get_product_by_id, get_all_products_db, delete_product_by_id
from app.repositories.product_type_repository import get_pt_by_id


def create_product(data):
    type_id = data.get('typeId', None)

    if not type_id:
        return jsonify({"message": "Please provide a type of product"}), 400

    type_ = get_pt_by_id(type_id)

    if type_.type == 'bike':
        return jsonify({"message": "Bike products are created when you're creating a bike"}), 400

    name = data.get('name', None)
    price = data.get('price', None)
    stock = data.get('stock', None)
    in_stock = False
    if stock > 0:
        in_stock = True

    new_product = Product(name=name, price=price, stock=stock, in_stock=in_stock, product_type=type_)
    db.session.add(new_product)
    db.session.commit()

    return jsonify({"message": "Product created successfully"}), 201


def delete_product(id):
    product = get_product_by_id(id)
    if product.product_type.type == "bike":
        return jsonify({"message": "Product with type bike is deleted when the related bike is deleted"}), 400
    delete_product_by_id(id)
    return jsonify({"message": "Product deleted successfully"}), 204


def update_product(id, data):
    type_id = data.get('typeId', None)

    if not type_id:
        return jsonify({"message": "Please provide a type of product"}), 400

    type_ = get_pt_by_id(type_id)

    if type_.type == 'bike':
        return jsonify({"message": "Bike products are updated when you're updating a bike"}), 400

    product = get_product_by_id(id)

    if not product:
        return jsonify({"message": "The product does not exist"}), 400

    name = data.get('name', None)
    price = data.get('price', None)
    stock = data.get('stock', None)
    in_stock = False
    if stock > 0:
        in_stock = True

    product.name = name
    product.price = price
    product.stock = stock
    product.in_stock = in_stock
    product.product_type = type_

    db.session.add(product)
    db.session.commit()

    return jsonify({"message": "Product updated successfully"}), 200


def get_product(id):
    product = get_product_by_id(id)
    return jsonify({
        "data": product.to_dict()}
    ), 200


def get_all_products():
    products = get_all_products_db()
    return jsonify({
        "data": [pt.to_dict() for pt in products]}
    ), 200
