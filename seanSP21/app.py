from flask import Flask
from flask_restful import Api
from flask_jwt_extended import JWTManager
from flask_cors import CORS
from db import db

## import all resources here
from resources.car import CarRegister, CarList, Car
from resources.user import UserRegister, UserList, User


app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///data.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
config = {
  'ORIGINS': [
    'http://localhost:3000',
  ],

  'SECRET_KEY': '...'
}

app.secret_key = 'builder'
api = Api(app)

@app.before_first_request
def create_tables():
  db.create_all()


jwt = JWTManager(app)

# add all resources below
api.add_resource(UserRegister, '/register')
api.add_resource(UserList, '/users')
api.add_resource(User, '/user/<string:username>')

api.add_resource(CarRegister, '/carregister')
api.add_resource(Car, '/car/<string:model>')
api.add_resource(CarList, '/cars')

CORS(app, resources={r'/*': {'origins': config['ORIGINS']}}, supports_credentials=True)

if __name__ == '__main__':
    db.init_app(app)
    app.run(port=5000, debug=True)