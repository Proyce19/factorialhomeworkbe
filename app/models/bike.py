from app.extensions import db

class Bike(db.Model):
    __tablename__ = "bike"
    __table_args__ = {'schema': 'fct'}

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String, nullable=False)
    frame_id = db.Column(db.Integer, db.ForeignKey('fct.frame.id'), nullable=False)
    wheel_id = db.Column(db.Integer, db.ForeignKey('fct.wheel.id'), nullable=False)
    rim_id = db.Column(db.Integer, db.ForeignKey('fct.rim.id'), nullable=False)
    chain_id = db.Column(db.Integer, db.ForeignKey('fct.chain.id'), nullable=False)
    product_id = db.Column(db.Integer, db.ForeignKey('fct.product.id'), nullable=False)
    price = db.Column(db.Float, nullable=False, default=0)
    stock = db.Column(db.Integer, nullable=False, default=0)
    in_stock = db.Column(db.Boolean, nullable=False, default=False)
    is_created_by_admin = db.Column(db.Boolean, nullable=False, default=True)
    is_created_by_user = db.Column(db.Boolean, nullable=False, default=False)
    creator_id = db.Column(db.Integer, db.ForeignKey('fct.fct_user.id'), nullable=False)

    # Relationships
    frame = db.relationship('Frame', back_populates='bikes', foreign_keys=[frame_id])
    wheel = db.relationship('Wheel', back_populates='bikes', foreign_keys=[wheel_id])
    rim = db.relationship('Rim', back_populates='bikes', foreign_keys=[rim_id])
    chain = db.relationship('Chain', back_populates='bikes', foreign_keys=[chain_id])
    product = db.relationship('Product', back_populates='bike', uselist=False)
    creator = db.relationship('User', back_populates='bikes', foreign_keys=[creator_id])

    def to_dict(self):
        return {"id": self.id,
                "name": self.name,
                "frame": self.frame.to_dict(),
                "rim": self.rim.to_dict(),
                "wheel": self.wheel.to_dict(),
                "chain": self.chain.to_dict(),
                "price": self.price,
                "stock": self.stock,
                "in_stock": self.in_stock,
                "product_id": self.product_id}


