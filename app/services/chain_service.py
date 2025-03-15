from flask import jsonify

from app import db
from app.models.chain import Chain
from app.repositories.chain_repository import get_chain_by_type, delete_chain_by_id, get_chain_by_id, get_all_chains_db


def create_chain(data):
    type_chain = data.get('type', None)
    price = data.get('price', 0)
    stock = data.get('stock', 0)
    in_stock = False

    if stock > 0:
        in_stock = True

    if not type_chain:
        return jsonify({"message": "Please provide type of chain"}), 422

    existing_chain = get_chain_by_type(type_chain)

    if existing_chain:
        return jsonify({"message": "The chain with the provided type already exist."}), 422

    new_chain = Chain(type=type_chain, price=price, in_stock=in_stock, stock=stock)
    db.session.add(new_chain)
    db.session.commit()

    return jsonify({"message": "Chain created successfully"}), 201


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
        return jsonify({"message": "Please provide type of chain"}), 422

    existing_chain = get_chain_by_id(id)

    if not existing_chain:
        return jsonify({"message": "Please provide existing chain"}), 422

    if existing_chain.type != type_chain:
        existing_chain_with_type = get_chain_by_type(type_chain)
        if existing_chain_with_type:
            return jsonify({"message": "The chain with the provided type already exist."}), 422
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
