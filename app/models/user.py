from app.extensions import db
from flask_login import UserMixin



class User(db.Model, UserMixin):
    __tablename__ = "fct_user"
    __table_args__ = {'schema': 'fct'}

    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(80), unique=True, nullable=False)
    password_hash = db.Column(db.String(256), nullable=False)
    is_admin = db.Column(db.Boolean, default=False, nullable=False)

    # Relationships
    carts = db.relationship('Cart', back_populates='user')
    bikes = db.relationship('Bike', back_populates='creator')

    def to_dict(self):
        return {"id": self.id, "username": self.username}
