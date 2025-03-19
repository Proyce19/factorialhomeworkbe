from flask import jsonify
from flask_jwt_extended import get_jwt_identity

from app import db
from app.models.cart import Cart
from app.models.product_cart import ProductCart
from app.repositories.cart_repository import delete_pc_by_cart_id, delete_cart_by_id, get_cart_by_id


def create_cart(data):
    products = data.get('products', [])
    user_id = get_jwt_identity()

    if len(products) == 0:
        return jsonify({"message": "Please provide product"}), 422

    total = sum([product.price for product in products])

    new_cart = Cart(total=total, is_purchased=False, is_abandoned=False, is_active=True, user_id=user_id)
    db.session.add(new_cart)
    for p in products:
        pc = ProductCart(product_id=p.id, cart_id=new_cart.id)
        db.session.add(pc)
    db.session.commit()

    return jsonify({"message": "Cart created successfully"}), 201


def delete_cart(id):
    delete_pc_by_cart_id(id)
    delete_cart_by_id(id)
    db.session.commit()
    return jsonify({"message": "Cart deleted successfully"}), 204


def update_cart(id, data):
    products = data.get('products', [])
    is_purchased = data.get('is_purchased', False)
    cart = get_cart_by_id(id)

    if not cart:
        jsonify({"message": "Please provide a valid cart"}), 422

    if len(products) == 0:
        cart.is_abandoned = True
        delete_cart_by_id(id)
        return jsonify({"message": "The cart is deleted since no products were provided"}), 204

    total = sum([product.price for product in products])

    cart.total = total

    if is_purchased:
        cart.is_purchased = True

    db.session.add(cart)
    for p in products:
        pc = ProductCart(product_id=p.id, cart_id=cart.id)
        db.session.add(pc)
    db.session.commit()

    return jsonify({"message": "Cart created successfully"}), 201


def get_cart(id):
    cart = get_cart_by_id(id)

    if cart:
        data = cart.to_dict()
    else:
        data = {}

    return jsonify({
        "data": data}
    ), 200
