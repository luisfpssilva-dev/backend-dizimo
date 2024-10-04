from flask import request, jsonify
from flask_restful import Resource
from src.services.comunidade_service import get_all_comunidades, get_comunidade_by_id, create_comunidade, update_comunidade, delete_comunidade

class ComunidadeResource(Resource):
    def get(self, client_id=None):
        if client_id:
            return get_comunidade_by_id(client_id)
        else:
            return get_all_comunidades()
    
    def post(self):
        data = request.get_json()
        new_client = create_comunidade(data)
        return new_client, 201
    
    def put(self, client_id):
        data = request.get_json()
        updated_client = update_comunidade(client_id, data)
        return updated_client
    
    def delete(self, client_id):
        delete_comunidade(client_id)
        return '', 204

def initialize_routes_comunidade(api):
    api.add_resource(ComunidadeResource, '/comunidade', '/comunidade/<string:comunidade_id>')
