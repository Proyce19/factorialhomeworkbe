from app.models.product import Product


def get_product_by_id(id):
    return Product.query.get(id)


def get_all_products_db():
    return Product.query.all()


def delete_product_by_id(id):
    Product.query.filter_by(id=id).delete()


def get_products_by_type_id(id):
    Product.query.filter_by(product_type_id=id).all()
