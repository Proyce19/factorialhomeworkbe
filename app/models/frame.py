from app import db


class Frame(db.Model):
    __tablename__ = 'frame'
    __table_args__ = {'schema': 'fct'}

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String, nullable=False)
    frame_finish_id = db.Column(db.Integer, db.ForeignKey('fct.frame_finish.id'), nullable=False)
    frame_type_id = db.Column(db.Integer, db.ForeignKey('fct.frame_type.id'), nullable=False)
    price = db.Column(db.Float, nullable=False, default=0)
    stock = db.Column(db.Integer, nullable=False, default=0)
    in_stock = db.Column(db.Boolean, nullable=False, default=False)

    # Relationships
    frame_finish = db.relationship('FrameFinish', back_populates='frames', foreign_keys=[frame_finish_id])
    frame_type = db.relationship('FrameFinish', back_populates='frames', foreign_keys=[frame_type_id])
    bikes = db.relationship('Bike', back_populates='frame')
    valid_combinations = db.relationship('ValidCombinations', back_populates='frame')

    def to_dict(self):
        return {"id": self.id,
                "name": self.name,
                "type": self.frame_type,
                "finish": self.frame_finish,
                "price": self.price,
                "stock": self.stock,
                "in_stock": self.in_stock}

    def update_stock(self, diff):
        self.stock -= diff
        self.frame_type.update_stock(diff)
        self.frame_finish.update_stock(diff)
        if self.stock == 0:
            self.in_stock = False
