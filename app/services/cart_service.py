from flask import jsonify
from flask_jwt_extended import get_jwt_identity

from app import db
from app.models.cart import Cart
from app.models.product_cart import ProductCart
from app.repositories.bike_repository import get_bike_by_product_id
from app.repositories.cart_repository import delete_pc_by_cart_id, delete_cart_by_id, get_cart_by_id, \
    get_cart_by_user_id
from app.repositories.product_repository import get_product_by_id


def create_cart(data):
    products = data.get('products', [])
    user_id = get_jwt_identity()

    existing_cart = get_cart_by_user_id(user_id)

    if existing_cart:
        return update_cart(existing_cart.id, data)
    else:
        if len(products) == 0:
            return jsonify({"message": "Please provide product"}), 422
        total = 0
        product_ids = []
        amounts = []
        for p in products:
            pid = int(p["id"])
            amount = int(p["amount"])
            product = get_product_by_id(pid)
            if product:
                if amount <= product.stock:
                    total += product.price * amount
                    if pid not in product_ids:
                        product_ids.append(pid)
                        amounts.append(amount)
                else:
                    return jsonify({"message": f"Product {product.name} has less stock than the provided amount"}), 422
            else:
                return jsonify({"message": "Please provide existing product"}), 422

        new_cart = Cart(total=total, is_purchased=False, is_abandoned=False, is_active=True, user_id=user_id)
        db.session.add(new_cart)
        for i, p_id in enumerate(product_ids):
            pc = ProductCart(product_id=p_id, cart=new_cart, amount=amounts[i])
            db.session.add(pc)
        db.session.commit()

        return jsonify({"message": "Cart created successfully"}), 201


def delete_cart(id):
    delete_pc_by_cart_id(id)
    delete_cart_by_id(id)
    db.session.commit()
    return jsonify({"message": "Cart deleted successfully"}), 200


def update_cart(id, data):
    products = data.get('products', [])
    is_purchased = data.get('is_purchased', False)
    cart = get_cart_by_id(id)

    if not cart:
        jsonify({"message": "Please provide a valid cart"}), 422

    if len(products) == 0:
        cart.is_abandoned = True
        return delete_cart(id)
        return jsonify({"message": "The cart is deleted since no products were provided"}), 200

    total = 0
    product_ids = []
    amounts = []
    products_obj = []
    for p in products:
        pid = int(p["id"])
        amount = int(p["amount"])
        product = get_product_by_id(pid)
        if product:
            if amount <= product.stock:
                total += product.price * amount
                if pid not in product_ids:
                    product_ids.append(pid)
                    amounts.append(amount)
                    products_obj.append(product)
            else:
                return jsonify({"message": f"Product {product.name} has less stock than the provided amount"}), 422
        else:
            return jsonify({"message": "Please provide existing product"}), 422

    cart.total = total

    if is_purchased:
        cart.is_purchased = True
        cart.is_active = False
        for i, p in enumerate(products_obj):
            p.stock -= amounts[i]
            if p.stock == 0:
                p.in_stock = False
            if p.product_type.type == "bike":
                bike = get_bike_by_product_id(p.id)
                if bike:
                    bike.stock -= amounts[i]
                    if bike.stock == 0:
                        bike.in_stock = False
                    db.session.add(bike)
            db.session.add(p)

    db.session.add(cart)
    delete_pc_by_cart_id(id)
    for i, p_id in enumerate(product_ids):
        pc = ProductCart(product_id=p_id, cart=cart, amount=amounts[i])
        db.session.add(pc)
    db.session.commit()

    return jsonify({"message": "Cart updated successfully"}), 201


def get_cart(id):
    cart = get_cart_by_id(id)

    if cart:
        data = cart.to_dict()
    else:
        data = {}

    return jsonify({
        "data": data}
    ), 200
