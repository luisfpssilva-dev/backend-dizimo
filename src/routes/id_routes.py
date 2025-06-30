from flask_restful import Resource
from src.services.titular_service import client_next_id, get_client_by_numero_dizimista


class TitularNextNumberResource(Resource):
    def get(self, id=None):
        if id is None:
            result = client_next_id()
            return result, 200
        else:
            client = get_client_by_numero_dizimista(id)

            if client is None:
                return client, 200
            else:
                return {'message': "Número já utilizado"}, 400



def initialize_routes_id(api):
    api.add_resource(TitularNextNumberResource, '/titular/id/', '/titular/id/<string:id>')
    