from app import db


class Cart(db.Model):
    __tablename__ = 'cart'
    __table_args__ = {'schema': 'fct'}

    id = db.Column(db.Integer, primary_key=True)
    total = db.Column(db.String, nullable=False)
    is_purchased = db.Column(db.Boolean, nullable=False, default=False)
    is_abandoned = db.Column(db.Boolean, nullable=False, default=False)
    is_active = db.Column(db.Boolean, nullable=False, default=False)
    user_id = db.Column(db.Integer, db.ForeignKey("fct.fct_user.id"), nullable=False)

    # Relationships
    product_carts = db.relationship('ProductCart', back_populates='cart')
    user = db.relationship('User', back_populates='carts', foreign_keys=[user_id])
