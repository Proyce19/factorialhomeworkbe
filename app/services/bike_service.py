from flask import jsonify
from flask_jwt_extended import get_jwt_identity

from app import db
from app.models.bike import Bike
from app.models.product import Product
from app.repositories.bike_repository import get_bike_by_all_attributes, delete_bike_by_id, get_bike_by_id, \
    get_all_bikes_db, get_all_bikes_created_by_admin_and_by_the_user
from app.repositories.chain_repository import get_chain_by_type, delete_chain_by_id, get_chain_by_id, get_all_chains_db
from app.repositories.frame_repository import get_frame_by_id
from app.repositories.product_type_repository import get_pt_by_type
from app.repositories.rim_repository import get_rim_by_id
from app.repositories.user_repository import get_user_by_id
from app.repositories.valid_combinations_repository import get_vc_by_all_attributes
from app.repositories.wheel_repository import get_wheel_by_id


def create_bike(data):
    user_id = get_jwt_identity()
    user = get_user_by_id(user_id)
    admin_flag = False
    if user.is_admin:
        admin_flag = True
    name = data.get('name', None)
    frame_id = data.get('frameId', None)
    wheel_id = data.get('wheelId', None)
    rim_id = data.get('rimId', None)
    chain_id = data.get('chainId', None)
    price = data.get('price', None)
    stock = data.get('stock', None)

    if not name:
        return jsonify({"message": "Please provide name for the bike"}), 422

    if not frame_id:
        return jsonify({"message": "Please provide frame"}), 422

    if not wheel_id:
        return jsonify({"message": "Please provide wheel"}), 422

    if not rim_id:
        return jsonify({"message": "Please provide rim"}), 422

    if not chain_id:
        return jsonify({"message": "Please provide chain"}), 422

    frame = get_frame_by_id(frame_id)
    if not frame:
        return jsonify({"message": "The provided frame does not exits"}), 422

    wheel = get_wheel_by_id(wheel_id)
    if not wheel:
        return jsonify({"message": "The provided wheel does not exits"}), 422

    rim = get_rim_by_id(rim_id)
    if not rim:
        return jsonify({"message": "The provided rim does not exits"}), 422

    chain = get_chain_by_id(chain_id)
    if not chain:
        return jsonify({"message": "The provided chain does not exits"}), 422

    existing_combination = get_vc_by_all_attributes(frame, wheel, rim, chain)

    if not existing_combination:
        return jsonify(
            {"message": "The combination with the provided frame, wheel, rim and chain does not exists"}), 422

    existing_bike = get_bike_by_all_attributes(frame, wheel, rim, chain)

    if existing_bike:
        return jsonify({"message": "The bike with the selected parts already exist. You can add it in your cart."}), 422

    if not any([frame.in_stock, wheel.in_stock, rim.in_stock, chain.in_stock]):
        return jsonify({"message": "Some of the parts are out of stock."}), 422

    stock_from_parts = min(frame.stock, wheel.stock, rim.stock, chain.stock)
    price_from_parts = frame.price + wheel.price + rim.price + chain.price

    if not price:
        price = price_from_parts

    if not stock:
        stock = stock_from_parts
    else:
        if stock > stock_from_parts:
            return jsonify(
                {"message": "The provided stock number is greater the the amount of available parts."}), 422

    in_stock = False
    if stock > 0:
        in_stock = True

    product_type = get_pt_by_type('bike')

    product = Product(name=f'BIKE-{name}', stock=stock, in_stock=in_stock, price=price, product_type=product_type)

    new_bike = Bike(name=name,
                    frame=frame,
                    chain=chain,
                    price=price,
                    in_stock=in_stock,
                    stock=stock,
                    is_created_by_admin=admin_flag,
                    is_created_by_user=not admin_flag,
                    creator_id=user_id,
                    product_id=product.id)
    frame.stock -= stock
    wheel.stock -= stock
    rim.stock -= stock
    chain.stock -= stock
    db.session.add_all([new_bike, frame, wheel, rim, chain, product])
    db.session.commit()

    return jsonify({"message": "Bike created successfully"}), 201


def delete_bike(id):
    user_id = get_jwt_identity()
    user = get_user_by_id(user_id)
    admin_flag = False
    if user.is_admin:
        admin_flag = True

    if admin_flag:
        bike = get_bike_by_id(id)
        delete_product_by_id(bike.product.id)
        delete_bike_by_id(id)
    else:
        bike = get_bike_by_id(id)
        if bike.creator_id == user:
            delete_product_by_id(bike.product.id)
            delete_bike_by_id(id)
        else:
            return jsonify({"message": "You can delete only the bikes you've created"}), 204
    return jsonify({"message": "Bike deleted successfully"}), 204


def update_bike(id, data):
    user_id = get_jwt_identity()
    user = get_user_by_id(user_id)
    admin_flag = False
    if user.is_admin:
        admin_flag = True
    name = data.get('name', None)
    frame_id = data.get('frameId', None)
    wheel_id = data.get('wheelId', None)
    rim_id = data.get('rimId', None)
    chain_id = data.get('chainId', None)
    price = data.get('price', None)
    stock = data.get('stock', None)

    bike = get_bike_by_id(id)

    if not bike:
        return jsonify({"message": "Please provide a valid bike"}), 422

    if not admin_flag:
        if bike.creator_id != user_id:
            return jsonify({"message": "You can update only the bikes you've created"}), 422

    if not name:
        return jsonify({"message": "Please provide name for the bike"}), 422

    if not frame_id:
        return jsonify({"message": "Please provide frame"}), 422

    if not wheel_id:
        return jsonify({"message": "Please provide wheel"}), 422

    if not rim_id:
        return jsonify({"message": "Please provide rim"}), 422

    if not chain_id:
        return jsonify({"message": "Please provide chain"}), 422

    frame = get_frame_by_id(frame_id)
    if not frame:
        return jsonify({"message": "The provided frame does not exits"}), 422

    wheel = get_wheel_by_id(wheel_id)
    if not wheel:
        return jsonify({"message": "The provided wheel does not exits"}), 422

    rim = get_rim_by_id(rim_id)
    if not rim:
        return jsonify({"message": "The provided rim does not exits"}), 422

    chain = get_chain_by_id(chain_id)
    if not chain:
        return jsonify({"message": "The provided chain does not exits"}), 422

    existing_combination = get_vc_by_all_attributes(frame, wheel, rim, chain)

    if not existing_combination:
        return jsonify(
            {"message": "The combination with the provided frame, wheel, rim and chain does not exists"}), 422

    existing_bike = get_bike_by_all_attributes(frame, wheel, rim, chain)

    is_using_same_parts = False
    if existing_bike.id == id:
        is_using_same_parts = True

    if existing_bike and existing_bike.id != id:
        return jsonify({"message": "The bike with the selected parts already exist. You can add it in your cart."}), 422

    if not is_using_same_parts:
        if not any([frame.in_stock, wheel.in_stock, rim.in_stock, chain.in_stock]):
            return jsonify({"message": "Some of the parts are out of stock."}), 422

        stock_from_parts = min(frame.stock, wheel.stock, rim.stock, chain.stock)
        price_from_parts = frame.price + wheel.price + rim.price + chain.price

        if not price:
            price = price_from_parts

        if not stock:
            stock = stock_from_parts
        else:
            if stock > stock_from_parts:
                return jsonify(
                    {"message": "The provided stock number is greater the the amount of available parts."}), 422

        in_stock = False
        if stock > 0:
            in_stock = True

        bike.name = name
        bike.stock = stock
        bike.in_stock = in_stock
        bike.price = price
        bike.frame = frame
        bike.wheel = wheel
        bike.rim = rim
        bike.chain = chain
        frame.stock -= stock
        wheel.stock -= stock
        rim.stock -= stock
        chain.stock -= stock
        db.session.add_all([bike, frame, wheel, rim, chain])
        db.session.commit()

    else:
        old_stock = bike.stock
        if stock > old_stock:
            difference = stock - old_stock
            stock_from_parts = min(frame.stock, wheel.stock, rim.stock, chain.stock)
            if difference > stock_from_parts:
                return jsonify(
                    {"message": "The provided stock number is greater the the amount of available parts."}), 422

            frame.stock -= difference
            wheel.stock -= difference
            rim.stock -= difference
            chain.stock -= difference
            bike.stock = stock
            in_stock = False
            if stock > 0:
                in_stock = True
            bike.in_stock = in_stock
            bike.name = name
            bike.price = price
            product = bike.product
            product.name = f'BIKE {bike.name}'
            product.stock = stock
            product.in_stock = in_stock
            product.price = price
            db.session.add_all([bike, frame, wheel, rim, chain, product])
            db.session.commit()
        elif stock < old_stock:
            difference = old_stock - stock
            frame.stock += difference
            wheel.stock += difference
            rim.stock += difference
            chain.stock += difference
            bike.stock = stock
            in_stock = False
            if stock > 0:
                in_stock = True
            bike.in_stock = in_stock
            bike.name = name
            bike.price = price
            product = bike.product
            product.name = f'BIKE {bike.name}'
            product.stock = stock
            product.in_stock = in_stock
            product.price = price
            db.session.add_all([bike, frame, wheel, rim, chain, product])
            db.session.commit()

    return jsonify({"message": "Bike updated successfully"}), 200


def get_bike(id):
    user_id = get_jwt_identity()
    user = get_user_by_id(user_id)
    admin_flag = False
    if user.is_admin:
        admin_flag = True
    bike = get_bike_by_id(id)
    if not admin_flag:
        if bike.is_created_by_user and bike.creator_id != user_id:
            return jsonify({"message": "You can only see details about your custom bikes"}), 200

    return jsonify({
        "data": bike.to_dict()}
    ), 200


def get_all_bikes():
    user_id = get_jwt_identity()
    user = get_user_by_id(user_id)
    admin_flag = False
    if user.is_admin:
        admin_flag = True

    if admin_flag:
        bikes = get_all_bikes_db()
    else:
        bikes = get_all_bikes_created_by_admin_and_by_the_user(user_id)
    return jsonify({
        "data": [bike.to_dict() for bike in bikes]}
    ), 200
