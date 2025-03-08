from flask import jsonify

from app import db
from app.models.bike import Bike
from app.models.chain import Chain
from app.repositories.chain_repository import get_chain_by_type, delete_chain_by_id, get_chain_by_id, get_all_chains_db
from app.repositories.frame_repository import get_frame_by_id
from app.repositories.rim_repository import get_rim_by_id
from app.repositories.valid_combinations_repository import get_vc_by_all_attributes
from app.repositories.wheel_repository import get_wheel_by_id


def create_bike(data):
    name = data.get('name', None)
    frame_id = data.get('frameId', None)
    wheel_id = data.get('wheelId', None)
    rim_id = data.get('rimId', None)
    chain_id = data.get('chainId', None)

    if not name:
        return jsonify({"message": "Please provide name for the bike"}), 400

    if not frame_id:
        return jsonify({"message": "Please provide frame"}), 400

    if not wheel_id:
        return jsonify({"message": "Please provide wheel"}), 400

    if not rim_id:
        return jsonify({"message": "Please provide rim"}), 400

    if not chain_id:
        return jsonify({"message": "Please provide chain"}), 400

    frame = get_frame_by_id(frame_id)
    if not frame:
        return jsonify({"message": "The provided frame does not exits"}), 400

    wheel = get_wheel_by_id(wheel_id)
    if not wheel:
        return jsonify({"message": "The provided wheel does not exits"}), 400

    rim = get_rim_by_id(rim_id)
    if not rim:
        return jsonify({"message": "The provided rim does not exits"}), 400

    chain = get_chain_by_id(chain_id)
    if not chain:
        return jsonify({"message": "The provided chain does not exits"}), 400

    existing_combination = get_vc_by_all_attributes(frame, wheel, rim, chain)

    if not existing_combination:
        return jsonify(
            {"message": "The combination with the provided frame, wheel, rim and chain does not exists"}), 400

    existing_bike = get_bike_by_all_attributes(frame, wheel, rim, chain)

    if existing_bike:
        return jsonify({"message": "The bike with the selected parts already exist. You can add it in your cart."}), 400

    stock = min(frame.stock, wheel.stock, rim.stock, chain.stock)
    price = frame.price + wheel.price + rim.price + chain.price
    in_stock = False
    if stock > 0:
        in_stock = True
    new_chain = Bike(name=name, frame=frame, chain=chain,  price=price, in_stock=in_stock, stock=stock)
    db.session.add(new_chain)
    db.session.commit()

    return jsonify({"message": "Bike created successfully"}), 201


def delete_chain(id):
    delete_chain_by_id(id)
    return jsonify({"message": "Chain deleted successfully"}), 204


def update_chain(id, data):
    type_chain = data.get('type', None)
    price = data.get('price', 0)
    stock = data.get('stock', 0)
    in_stock = False

    if stock > 0:
        in_stock = True

    if not type_chain:
        return jsonify({"message": "Please provide type of chain"}), 400

    existing_chain = get_chain_by_id(id)

    if not existing_chain:
        return jsonify({"message": "Please provide existing chain"}), 400

    if existing_chain.type != type_chain:
        existing_chain_with_type = get_chain_by_type(type_chain)
        if existing_chain_with_type:
            return jsonify({"message": "The chain with the provided type already exist."}), 400
        existing_chain.type = type_chain

    existing_chain.price = price
    existing_chain.stock = stock
    existing_chain.in_stock = in_stock

    db.session.add(existing_chain)
    db.session.commit()

    return jsonify({"message": "Chain updated successfully"}), 200


def get_chain(id):
    chain = get_chain_by_id(id)
    return jsonify({
        "data": chain.to_dict()}
    ), 200


def get_all_chains():
    chains = get_all_chains_db()
    return jsonify({
        "data": [chain.to_dict() for chain in chains]}
    ), 200
