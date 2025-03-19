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

    def to_dict(self):
        return {"id": self.id,
                "total": self.total,
                "is_purchased": self.is_purchased,
                "is_abandoned": self.is_abandoned,
                "is_active": self.is_active,
                "user": self.user.username}

    # Relationships
    product_carts = db.relationship('ProductCart', back_populates='cart')
    user = db.relationship('User', back_populates='carts', foreign_keys=[user_id])
