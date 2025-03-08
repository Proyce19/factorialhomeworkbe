from app import db


class Wheel(db.Model):
    __tablename__ = 'wheel'
    __table_args__ = {'schema': 'fct'}

    id = db.Column(db.Integer, primary_key=True)
    type = db.Column(db.String, nullable=False)
    price = db.Column(db.Float, nullable=False, default=0)
    in_stock = db.Column(db.Boolean, nullable=False, default=False)
    stock = db.Column(db.Integer, nullable=False, default=0)

    # Relationships
    bikes = db.relationship('Bike', back_populates='wheel')
    valid_combinations = db.relationship('ValidCombinations', back_populates='wheel')

    def to_dict(self):
        return {"id": self.id,
                "type": self.type,
                "price": self.price,
                "stock": self.stock,
                "in_stock": self.in_stock}


    def update_stock(self, diff):
        self.stock -= diff
        if self.stock == 0:
            self.in_stock = False
