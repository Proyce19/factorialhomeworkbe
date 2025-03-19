from app import db


class ProductCart(db.Model):
    __tablename__ = 'product_cart'
    __table_args__ = {'schema': 'fct'}

    id = db.Column(db.Integer, primary_key=True)

    product_id = db.Column(db.Integer, db.ForeignKey('fct.product.id'), nullable=False)
    cart_id = db.Column(db.Integer, db.ForeignKey('fct.cart.id'), nullable=False)

    # Relationships
    product = db.relationship('Product', back_populates='product_carts', foreign_keys=[product_id])
    cart = db.relationship('Cart', back_populates='product_carts', foreign_keys=[cart_id])


