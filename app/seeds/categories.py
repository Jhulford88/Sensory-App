from app.models import db, environment, SCHEMA
from sqlalchemy.sql import text
from app.models.categories import Category


def seed_categories():
    restaurant = Category(
        type = "Restaurant")
    shopping = Category(
        type = "Shopping")
    entertainment = Category(
        type = "Entertainment")
    other = Category(
        type = "Other")

    db.session.add(restaurant)
    db.session.add(shopping)
    db.session.add(entertainment)
    db.session.add(other)
    db.session.commit()


def undo_categories():
    if environment == "production":
        db.session.execute(f"TRUNCATE table {SCHEMA}.categories RESTART IDENTITY CASCADE;")
    else:
        db.session.execute(text("DELETE FROM categories"))

    db.session.commit()
