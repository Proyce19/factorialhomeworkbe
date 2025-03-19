from app import db


class Product(db.Model):
    __tablename__ = 'product'
    __table_args__ = {'schema': 'fct'}

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String, nullable=False)
    product_type_id = db.Column(db.Integer, db.ForeignKey('fct.product_type.id'), nullable=False)
    stock = db.Column(db.Integer, nullable=False, default=0)
    price = db.Column(db.Float, nullable=False, default=0)
    in_stock = db.Column(db.Boolean, nullable=False, default=False)

    # Relationships
    product_type = db.relationship('ProductType', back_populates='products')
    bike = db.relationship('Bike', back_populates='product', uselist=False)
    product_carts = db.relationship('ProductCart', back_populates='product')

    def to_dict(self):
        return {"id": self.id,
                "name": self.name,
                "price": self.price,
                "stock": self.stock,
                "in_stock": self.in_stock}

    def update_stock(self, diff):
        self.stock -= diff
        self.bike.update_stock(diff)
        if self.stock == 0:
            self.in_stock = False
