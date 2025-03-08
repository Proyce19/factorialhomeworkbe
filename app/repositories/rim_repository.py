from app.models.rim import Rim


def get_rim_by_id(id):
    return Rim.query.get(id)


def get_rim_by_color(color):
    return Rim.query.filter_by(color=color).first()


def delete_rim_by_id(id):
    Rim.query.filter_by(id=id).delete()


def get_all_rims_db():
    return Rim.query.all()
