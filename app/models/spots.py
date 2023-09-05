from .db import db, environment, SCHEMA, add_prefix_for_prod


class Spot(db.Model):
    __tablename__ = 'spots'

    if environment == "production":
        __table_args__ = {'schema': SCHEMA}

    id = db.Column(db.Integer, primary_key=True)
    spot_name = db.Column(db.String(55), nullable=False, unique=True)
    address = db.Column(db.String(55), nullable=False)
    city = db.Column(db.String(55), nullable=False)
    state = db.Column(db.String(2), nullable=False)
    # category_id = db.Column(db.Integer, db.ForeignKey(
    #     add_prefix_for_prod("categories.id")), nullable=False)
    user_id = db.Column(db.Integer, db.ForeignKey(
        add_prefix_for_prod("users.id")), nullable=False)
    cover_photo = db.Column(db.String, nullable=False)
    description = db.Column(db.Text, nullable=False)

   #Relationships
    # category = db.relationship("Category",back_populates="spot")
    # reviews = db.relationship('Review', back_populates='spot', cascade="all, delete")
    user = db.relationship('User')



    def to_dict(self):
        return {
            'id': self.id,
            'SpotName': self.spot_name,
            'address': self.address,
            'city': self.city,
            'state': self.state,
            # 'categoryId': self.category_id,
            'coverPhoto': self.cover_photo,
            'userId':self.user_id,
            # "photos": [photo.to_dict() for photo in self.trail_photos],
            "description": self.description,
            # "reviews": [review.to_dict() for review in self.reviews]
        }
