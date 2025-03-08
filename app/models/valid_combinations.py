from app import db


class ValidCombinations(db.Model):
    __tablename__ = 'valid_combinations'
    __table_args__ = {'schema': 'fct'}

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String, nullable=False)
    frame_id = db.Column(db.Integer, db.ForeignKey('fct.frame.id'), nullable=False)
    wheel_id = db.Column(db.Integer, db.ForeignKey('fct.wheel.id'), nullable=False)
    rim_id = db.Column(db.Integer, db.ForeignKey('fct.rim.id'), nullable=False)
    chain_id = db.Column(db.Integer, db.ForeignKey('fct.chain.id'), nullable=False)

    # Relationships
    frame = db.relationship('Frame', back_populates='valid_combinations', foreign_keys=[frame_id])
    wheel = db.relationship('Wheel', back_populates='valid_combinations', foreign_keys=[wheel_id])
    rim = db.relationship('Rim', back_populates='valid_combinations', foreign_keys=[rim_id])
    chain = db.relationship('Chain', back_populates='valid_combinations', foreign_keys=[chain_id])


