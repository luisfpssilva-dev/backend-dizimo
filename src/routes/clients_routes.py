from flask import request, jsonify
from flask_restful import Resource
from src.services.clients_service import get_all_clients, get_client_by_id, create_client, update_client, delete_client

class ClientResource(Resource):
    def get(self, client_id=None):
        if client_id:
            return jsonify(get_client_by_id(client_id))
        else:
            return jsonify(get_all_clients())
    
    def post(self):
        data = request.get_json()
        return jsonify(create_client(data)), 201
    
    def put(self, client_id):
        data = request.get_json()
        return jsonify(update_client(client_id, data))
    
    def delete(self, client_id):
        delete_client(client_id)
        return '', 204

def initialize_routes(api):
    api.add_resource(ClientResource, '/clients', '/clients/<int:client_id>')
