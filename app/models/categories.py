from .db import db, environment, SCHEMA

class Category(db.Model):
    __tablename__ = "categories"

    if environment == "production":
        __table_args__ = {'schema': SCHEMA}


    id = db.Column(db.Integer, primary_key=True)
    type = db.Column(db.String(50),nullable=False,unique=True)

    spot = db.relationship("Spot",back_populates="category")

    def to_dict(self):
        return{
            "id":self.id,
            "type":self.type,
            }
