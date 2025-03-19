from sqlalchemy import or_

from app.models.bike import Bike


def get_bike_by_all_attributes(frame, wheel, rim, chain):
    return Bike.query.filter_by(frame=frame, wheel=wheel, rim=rim, chain=chain).first()


def get_bike_by_id(id):
    return Bike.query.get(id)


def delete_bike_by_id(id):
    Bike.query.filter_by(id=id).delete()


def get_all_bikes_db():
    return Bike.query.all()


def get_all_bikes_created_by_admin_and_by_the_user(id):
    return Bike.query.filter(or_(Bike.is_created_by_admin, Bike.creator_id == id)).all()


def get_bikes_by_chain_id(id):
    return Bike.query.filter_by(chain_id=id).all()


def get_bikes_by_wheel_id(id):
    return Bike.query.filter_by(wheel_id=id).all()


def get_bikes_by_frame_id(id):
    return Bike.query.filter_by(frame_id=id).all()


def get_bikes_by_rim_id(id):
    return Bike.query.filter_by(rim_id=id).all()


def get_bikes_by_product_id(id):
    return Bike.query.filter_by(product_id=id).all()


def get_bike_by_product_id(id):
    return Bike.query.filter_by(product_id=id).first()
