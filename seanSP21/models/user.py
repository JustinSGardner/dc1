import sqlite3
from db import db

class UserModel(db.Model):
    __tablename__ = 'users'

    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(80))
    password = db.Column(db.String(80))
    user_type = db.Column(db.String(80))
    first_name = db.Column(db.String(80))
    last_name = db.Column(db.String(80))
    

    def __init__(self, username, password, user_type, first_name, last_name):
        self.username = username
        self.password = password
        self.user_type = user_type
        self.first_name = first_name
        self.last_name = last_name


    def json(self):
        return {'user': self.id, 'username': self.username, 
                'first_name': self.first_name, 'last_name': self.last_name, 
                'user_type': self.user_type}
    
    def json2(self):
        return {'user': self.username, 'reports': [report.json() for report in self.report.all()]}


    @classmethod
    def find_by_username(cls, username):
        return cls.query.filter_by(username=username).first()

    @classmethod
    def find_by_id(cls, _id):
        return cls.query.filter_by(id=_id).first()

    def save_to_db(self):
        db.session.add(self)
        db.session.commit()

    def delete_from_db(self):
        db.session.delete(self)
        db.session.commit()