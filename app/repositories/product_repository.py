from app.models.product import Product


def get_product_by_id(id):
    return Product.query.get(id)


def get_all_products_db():
    return Product.query.all()


def delete_product_by_id(id):
    Product.query.filter_by(id).delete()
