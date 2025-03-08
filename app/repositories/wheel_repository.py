from app.models.wheel import Wheel


def get_wheel_by_id(id):
    return Wheel.query.get(id)


def get_wheel_by_type(type):
    return Wheel.query.filter_by(type=type).first()


def delete_wheel_by_id(id):
    Wheel.query.filter_by(id=id).delete()


def get_all_wheels_db():
    return Wheel.query.all()
