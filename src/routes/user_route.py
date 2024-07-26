from flask import request, jsonify, make_response
from flask_restful import Resource
from flask_jwt_extended import create_access_token
from src.services.users_service import create_user, authenticate_user

class UserRegistration(Resource):
    def post(self):
        data = request.get_json()
        try:
            user = create_user(data)
            return make_response(jsonify(user), 201)
        except ValueError as e:
            return make_response(jsonify({'message': str(e)}), 400)

class UserLogin(Resource):
    def post(self):
        data = request.get_json()
        try:
            user = authenticate_user(data['username'], data['password'])
            access_token = create_access_token(identity=user['id'])
            return make_response(jsonify(token=access_token), 200)
        except ValueError as e:
            return make_response(jsonify({'message': str(e)}), 400)

def initialize_user_routes(api):
    api.add_resource(UserRegistration, '/register')
    api.add_resource(UserLogin, '/login')
