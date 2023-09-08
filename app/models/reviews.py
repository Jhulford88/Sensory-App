from .db import db, environment, SCHEMA, add_prefix_for_prod
from datetime import date

class Review(db.Model):
    __tablename__ = "reviews"

    if environment == "production":
        __table_args__ = {'schema': SCHEMA}


    id = db.Column(db.Integer, primary_key=True)
    review_text = db.Column(db.Text, nullable=False)
    star_rating = db.Column(db.Integer, nullable=False)
    sight = db.Column(db.Integer, nullable=False)
    smell = db.Column(db.Integer, nullable=False)
    sound = db.Column(db.Integer, nullable=False)
    taste = db.Column(db.Integer, nullable=False)
    touch = db.Column(db.Integer, nullable=False)
    user_id = db.Column(db.Integer, db.ForeignKey(add_prefix_for_prod('users.id')), nullable=False)
    spot_id = db.Column(db.Integer, db.ForeignKey(add_prefix_for_prod('spots.id')), nullable=False)
    created_at = db.Column(db.Date, nullable=False, default=date.today())

    # Relationships
    users = db.relationship('User', back_populates='reviews')
    spots = db.relationship('Spot', back_populates='reviews', cascade="all, delete")

    def to_dict(self):
        return{
            "id": self.id,
            "reviewText": self.review_text,
            "starRating": self.star_rating,
            "sight": self.sight,
            "smell": self.smell,
            "sound": self.sound,
            "taste": self.taste,
            "touch": self.touch,
            "userId": self.user_id,
            "spotId": self.spot_id,
            "createdAt": self.created_at.strftime("%B %d, %Y"),
            "user": self.users.reviews_to_dict()["username"]
            }
