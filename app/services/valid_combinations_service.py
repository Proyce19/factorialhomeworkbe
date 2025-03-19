from flask import jsonify

from app import db
from app.models.valid_combinations import ValidCombinations
from app.repositories.chain_repository import get_chain_by_id
from app.repositories.frame_repository import get_frame_by_id
from app.repositories.rim_repository import get_rim_by_id
from app.repositories.valid_combinations_repository import get_vc_by_all_attributes, delete_vc_by_id, get_all_vcs_db
from app.repositories.wheel_repository import get_wheel_by_id


def create_vc(data):
    name = data.get('name', None)
    frame_id = data.get('frameId', None)
    wheel_id = data.get('wheelId', None)
    rim_id = data.get('rimId', None)
    chain_id = data.get('chainId', None)

    if not name:
        return jsonify({"message": "Please provide name for the combination"}), 422

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

    if existing_combination:
        return jsonify({"message": "The combination with the provided frame, wheel, rim and chain exists"}), 422

    new_combination = ValidCombinations(name=name, frame=frame, wheel=wheel, rim=rim, chain=chain)
    db.session.add(new_combination)
    db.session.commit()

    return jsonify({"message": "Combination created successfully"}), 201


def delete_vc(id):
    delete_vc_by_id(id)
    db.session.commit()
    return jsonify({"message": "Combination deleted successfully"}), 204


def get_all_vcs():
    vcs = get_all_vcs_db()

    if vcs:
        if len(vcs) > 0:
            data = [vc.to_dict() for vc in vcs]
        else:
            data = []
    else:
        data = []

    return jsonify({
        "data": data}
    ), 200
