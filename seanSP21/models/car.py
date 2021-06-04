import sqlite3
from db import db

class CarModel(db.Model):
    __tablename__ = 'cars'

    id = db.Column(db.Integer, primary_key=True)
    make = db.Column(db.String(80))
    model = db.Column(db.String(80))
    color = db.Column(db.String(80))
    doors = db.Column(db.String(80))
    top_speed = db.Column(db.String(10))
    zero_to_60 = db.Column(db.String(10))
    horsepower = db.Column(db.String(10))

    def __init__(self, make, model, color, doors, top_speed, zero_to_60, horsepower):
        self.make = make
        self.model = model
        self.color = color
        self.doors = doors
        self.top_speed = top_speed
        self.zero_to_60 = zero_to_60
        self.horsepower = horsepower

    def json(self):
        return {'vehicle_id': self.id, 'make': self.make, 'model': self.model,
                'color': self.color, 'doors': self.doors, 'top_speed': self.top_speed,
                'zero_to_60': self.zero_to_60, 'horsepower': self.horsepower}

    @classmethod
    def find_by_id(cls, _id):
        return cls.query.filter_by(id=_id).first()
    
    @classmethod
    def find_by_model(cls, model):
        return cls.query.filter_by(model=model).first()
    
    def save_to_db(self):
        db.session.add(self)
        db.session.commit()
    
    def delete_from_db(self):
        db.session.delete(self)
        db.session.commit()

