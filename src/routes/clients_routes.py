from flask import request, jsonify
from flask_restful import Resource
from src.services.clients_service import get_all_clients, get_client_by_id, create_client, update_client, delete_client

class ClientResource(Resource):
    def get(self, client_id=None):
        if client_id:
            return get_client_by_id(client_id)
        else:
            return get_all_clients()
    
    def post(self):
        data = request.get_json()
        new_client = create_client(data)
        return new_client, 201
    
    def put(self, client_id):
        data = request.get_json()
        updated_client = update_client(client_id, data)
        return updated_client
    
    def delete(self, client_id):
        delete_client(client_id)
        return '', 204

def initialize_routes(api):
    api.add_resource(ClientResource, '/clients', '/clients/<int:client_id>')
