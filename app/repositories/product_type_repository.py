from app.models.product_type import ProductType


def get_pt_by_id(id):
    return ProductType.query.get(id)


def get_pt_by_type(type):
    return ProductType.query.filter_by(type=type).first()


def delete_pt_by_id(id):
    ProductType.query.filter_by(id=id).delete()


def get_all_pts_db():
    return ProductType.query.all()
