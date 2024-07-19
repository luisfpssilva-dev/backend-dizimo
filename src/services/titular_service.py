from models.titular_model import TitularModel as Titular
from src.db import db

def get_all_clients():
    return [client.to_dict() for client in Titular.query.all()]

def get_client_by_id(titular_id):
    client = Titular.query.get_or_404(titular_id)
    return client.to_dict()

def create_titular(data):
    new_titular = Titular(
        numero_dizimista=data['numero_dizimista'],
        nome=data['nome'],
        telefone=data['telefone'],
        sexo=data['sexo'],
        data_nascimento=data['data_nascimento'],
        cpf=data['cpf'],
        email=data['email'],
        comunidade_id=data['comunidade_id']
    )
    db.session.add(new_titular)
    db.session.commit()
    return new_titular.to_dict()

def update_client(titular_id, data):
    client = Titular.query.get_or_404(titular_id)
    client.nome = data['nome']
    client.email = data['email']
    client.telefone = data['telefone']
    db.session.commit()
    return client.to_dict()

def delete_client(titular_id):
    client = Titular.query.get_or_404(titular_id)
    db.session.delete(client)
    db.session.commit()
    return '', 204
