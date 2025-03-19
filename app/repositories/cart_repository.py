from app.models.cart import Cart
from app.models.product_cart import ProductCart


def get_cart_by_id(id):
    return Cart.query.filter_by(id=id, is_purchased=False, is_abandoned=False).first()


def delete_cart_by_id(id):
    Cart.query.filter_by(id=id).delete()


def delete_pc_by_cart_id(cart_id):
    ProductCart.query.filter_by(cart_id=cart_id).delete()
