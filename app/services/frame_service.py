from flask import jsonify

from app import db
from app.models.frame import Frame
from app.repositories.bike_repository import get_bikes_by_frame_id
from app.repositories.frame_finish_repository import get_ff_by_id
from app.repositories.frame_repository import get_frame_by_type_and_finish, delete_frame_by_id, get_frame_by_id, \
    get_all_frames_db
from app.repositories.frame_type_repository import get_ft_by_id
from app.repositories.valid_combinations_repository import get_vcs_by_frame_id


def create_frame(data):
    name = data.get('name', None)
    price = data.get('price', 0)
    stock = data.get('stock', 0)
    frame_finish_id = data.get('frameFinishId', None)
    frame_type_id = data.get('frameTypeId', None)
    in_stock = False

    if stock > 0:
        in_stock = True

    if not name:
        return jsonify({"message": "Please provide name for the frame"}), 422

    if not frame_finish_id:
        return jsonify({"message": "Please provide frame finish"}), 422

    if not frame_type_id:
        return jsonify({"message": "Please provide frame type"}), 422

    frame_finish = get_ff_by_id(frame_finish_id)
    if not frame_finish:
        return jsonify({"message": "The provided frame finish does not exits"}), 422

    frame_type = get_ft_by_id(frame_type_id)
    if not frame_type:
        return jsonify({"message": "The provided frame type does not exits"}), 422


    existing_frame = get_frame_by_type_and_finish(frame_type, frame_finish)

    if existing_frame:
        return jsonify({"message": "The frame with the provided type and finish exist"}), 422

    new_frame = Frame(name=name, frame_finish=frame_finish, frame_type=frame_type, price=price, in_stock=in_stock, stock=stock)
    db.session.add(new_frame)
    db.session.commit()

    return jsonify({"message": "Frame created successfully"}), 201


def delete_frame(id):
    bikes = get_bikes_by_frame_id(id)
    if bikes and len(bikes) > 0:
        return jsonify({"message": "Frame cannot be deleted"}), 422
    vcs = get_vcs_by_frame_id(id)
    if vcs and len(vcs) > 0:
        return jsonify({"message": "Frame cannot be deleted"}), 422
    delete_frame_by_id(id)
    db.session.commit()
    return jsonify({"message": "Frame deleted successfully"}), 200


def update_frame(id, data):
    name = data.get('name', None)
    price = data.get('price', 0)
    stock = data.get('stock', 0)
    frame_finish_id = data.get('frameFinishId', None)
    frame_type_id = data.get('frameTypeId', None)
    in_stock = False

    if stock > 0:
        in_stock = True

    if not name:
        return jsonify({"message": "Please provide name for the frame"}), 422

    if not frame_finish_id:
        return jsonify({"message": "Please provide frame finish"}), 422

    if not frame_type_id:
        return jsonify({"message": "Please provide frame type"}), 422

    frame_finish = get_ff_by_id(frame_finish_id)
    if not frame_finish:
        return jsonify({"message": "The provided frame finish does not exits"}), 422

    frame_type = get_ft_by_id(frame_type_id)
    if not frame_type:
        return jsonify({"message": "The provided frame type does not exits"}), 422


    existing_frame = get_frame_by_id(id)

    if not existing_frame:
        return jsonify({"message": "Please provide existing frame"}), 422

    if existing_frame.frame_finish != frame_finish or existing_frame.frame_type != frame_type:
        existing_frame_with_type_and_finish = get_frame_by_type_and_finish(frame_type, frame_finish)
        if existing_frame_with_type_and_finish:
            return jsonify({"message": "The Frame with the provided type and finish already exists"}), 422
        existing_frame.frame_type = frame_type
        existing_frame.frame_finish = frame_finish

    existing_frame.price = price
    existing_frame.stock = stock
    existing_frame.in_stock = in_stock

    db.session.add(existing_frame)
    db.session.commit()

    return jsonify({"message": "Frame updated successfully"}), 200


def get_frame(id):
    frame = get_frame_by_id(id)

    if frame:
        data = frame.to_dict()
    else:
        data = {}

    return jsonify({
        "data": data}
    ), 200


def get_all_frames():
    frames = get_all_frames_db()

    if frames:
        if len(frames) > 0:
            data = [frame.to_dict() for frame in frames]
        else:
            data = []
    else:
        data = []

    return jsonify({
        "data": data}
    ), 200
