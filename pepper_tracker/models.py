from pepper_tracker import db
from flask_login import UserMixin
from datetime import date

class PepperPlant(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    plant_type = db.Column(db.String(50), nullable=False)
    sowing_date = db.Column(db.Date, nullable=False)
    seeds = db.Column(db.Integer, nullable=False)
    germinated = db.Column(db.Integer, nullable=False)
    seedlings = db.Column(db.Integer, nullable=False)
    hardening = db.Column(db.Integer, nullable=False)
    plants = db.Column(db.Integer, nullable=False)
    year = db.Column(db.Integer, nullable=False)
    dead = db.Column(db.Integer, default=0)  # Number of plants that died
    fruits = db.Column(db.Integer, default=0)  # Number of fruits produced

    def __repr__(self):
        return f'<PepperPlant {self.plant_type} ({self.year})>'


    def __repr__(self):
        return f'<PepperPlant {self.plant_type} ({self.year})>'


class User(db.Model, UserMixin):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(50), unique=True, nullable=False)
    password = db.Column(db.String(200), nullable=False)  # Note: In production, use password hashing!

    def __repr__(self):
        return f'<User {self.username}>'
