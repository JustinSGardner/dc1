from flask_restful import Resource, reqparse
from models.car import CarModel
# from flask_jwt_extended import jwt_required


class CarRegister(Resource):
    parser = reqparse.RequestParser()
    parser.add_argument('make',
            type=str,
            required=True,
            help="This field cannot be blank!"
    )
    parser.add_argument('model',
            type=str,
            required=True,
            help="This field cannot be blank!"
    )
    parser.add_argument('color',
            type=str,
            required=True,
            help="This field cannot be blank!"
    )
    parser.add_argument('doors',
            type=str,
            required=True,
            help="This field cannot be blank!"
    )
    parser.add_argument('top_speed',
            type=str,
            required=True,
            help="This field cannot be blank!"
    )
    parser.add_argument('zero_to_60',
            type=str,
            required=True,
            help="This field cannot be blank!"
    )
    parser.add_argument('horsepower',
            type=str,
            required=True,
            help="This field cannot be blank!"
    )

    def post(self):
        data = CarRegister.parser.parse_args()

        if CarModel.find_by_model(data['model']):
          return {'message': "Success"}, 400
        # if CarModel.find_by_model(data['model']):
        #     return {'message': "Car already exists!"}, 400

        car = CarModel(**data)
        car.save_to_db()

        return {'message': "Car created successfully."}, 201

class Car(Resource):
    parser = reqparse.RequestParser()
    parser.add_argument('make',
            type=str,
            required=True,
            help="This field cannot be blank!"
    )
    parser.add_argument('model',
            type=str,
            required=True,
            help="This field cannot be blank!"
    )
    parser.add_argument('color',
            type=str,
            required=True,
            help="This field cannot be blank!"
    )
    parser.add_argument('doors',
            type=str,
            required=True,
            help="This field cannot be blank!"
    )
    parser.add_argument('top_speed',
            type=str,
            required=True,
            help="This field cannot be blank!"
    )
    parser.add_argument('zero_to_60',
            type=str,
            required=True,
            help="This field cannot be blank!"
    )
    parser.add_argument('horsepower',
            type=str,
            required=True,
            help="This field cannot be blank!"
    )

    
    def get(self, model):
        car = CarModel.find_by_model(model)
        if car:
            return car.json()
        return {'message': "Car not found!"}, 404

    def put(self, model):
        data = Car.parser.parse_args()

        car = CarModel.find_by_model(model)

        if car is None:
            car = CarModel(car, **data)
        else:
            car.model = model
            car.make = data['make']
            car.color = data['color']
            car.doors = data['doors']
            car.top_speed = data['top_speed']
            car.zero_to_60 = data['zero_to_60']
            car.horsepower = data['horsepower']

        car.save_to_db()

        return car.json()

    def delete(self, model):
        car = CarModel.find_by_model(model)
        if car is None:
            return {'message': 'User not found!'}, 404
        else:
            car.delete_from_db()
            return {'message': 'User deleted!'}


class CarList(Resource):
    def get(self):
        return {'cars': [car.json() for car in CarModel.query.all()]}




