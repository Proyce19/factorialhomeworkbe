from app import db


class ProductType(db.Model):
    __tablename__ = 'product_type'
    __table_args__ = {'schema': 'fct'}

    id = db.Column(db.Integer, primary_key=True)
    type = db.Column(db.String, nullable=False)

    # Relationships
    products = db.relationship('Product', back_populates='product_type')

