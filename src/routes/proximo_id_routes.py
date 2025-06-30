from flask_restful import Resource
from src.services.titular_service import client_next_id


class TitularNextNumberResource(Resource):
    def get(self):
        result = client_next_id()
        return result, 200


def initialize_routes_proximo_id(api):
    api.add_resource(TitularNextNumberResource, '/titular/proximo_id/')
    