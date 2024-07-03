from src.models.clients_model import Client
from src.db import db

def get_all_clients():
    return [client.to_dict() for client in Client.query.all()]

def get_client_by_id(client_id):
    client = Client.query.get_or_404(client_id)
    return client.to_dict()

def create_client(data):
    new_client = Client(
        name=data['nome'],
        email=data['email'],
        phone=data['telefone']
    )
    db.session.add(new_client)
    db.session.commit()
    return new_client.to_dict()

def update_client(client_id, data):
    client = Client.query.get_or_404(client_id)
    client.name = data['nome']
    client.email = data['email']
    client.phone = data['telefone']
    db.session.commit()
    return client.to_dict()

def delete_client(client_id):
    client = Client.query.get_or_404(client_id)
    db.session.delete(client)
    db.session.commit()
    return '', 204
