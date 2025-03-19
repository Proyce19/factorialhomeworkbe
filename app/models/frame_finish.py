from app import db

class FrameFinish(db.Model):
    __tablename__ = 'frame_finish'
    __table_args__ = {'schema': 'fct'}

    id = db.Column(db.Integer, primary_key=True)
    type = db.Column(db.String, nullable=False)
    price = db.Column(db.Float, nullable=False, default=0)
    stock = db.Column(db.Integer, nullable=False, default=0)
    in_stock = db.Column(db.Boolean, nullable=False, default=False)

    # Relationships
    frames = db.relationship('Frame', back_populates='frame_finish')

    def to_dict(self):
        return {"id": self.id,
                "type": self.type,
                "price": self.price,
                "stock": self.stock,
                "in_stock": self.in_stock}



