from src.models import TitularModel as Titular
from datetime import datetime
from src.db import db
import uuid
import random


def get_all_clients():
    return [client.to_dict() for client in Titular.query.all()]


# def get_client_by_id(titular_id):
#     client = Titular.query.get_or_404(titular_id)
#     return client.to_dict()

def get_client_by_id(titular_id):
    # Consulta o titular pelo ID
    titular = db.session.query(Titular).filter_by(titular_id=titular_id).first()
    
    if not titular:
        return None

    # Converte o titular para dicionário, incluindo dependentes
    titular_data = titular.to_dict()
    titular_data['dependentes'] = [dependente.to_dict() for dependente in titular.dependente]

    return titular_data


def get_client_by_cpf(cpf):
    client = Titular.query.get_or_404(cpf)
    return client.to_dict()


def get_client_by_numero_dizimista(numero_dizimista):
    client = Titular.query.filter(Titular.numero_dizimista == numero_dizimista,
                                  Titular.deleted_at.is_(None)).first()
    if not client:
        return None
    return client.to_dict()


def create_titular(data):
    new_titular = Titular(
        titular_id = str(uuid.uuid4()),
        numero_dizimista=data['numero_dizimista'],
        name=data['name'],
        telefone=data['telefone'],
        sexo=data['sexo'],
        data_nascimento = datetime.strptime(data['data_nascimento'], '%Y-%m-%d').date(),
        cpf=data['cpf'],
        email=data['email'],
        comunidade_id=data['comunidade_id'],
        user_id = data['user_id']
    )
    db.session.add(new_titular)
    db.session.commit()
    #TODO VERIFICAR SE O ID ADICIONADO MAUNALMENTE JÁ EXISTE
    #TODO fazer verificacao de numero de dizimista e cpf
    return new_titular.to_dict()

def update_client(titular_id, data):
    client = Titular.query.get_or_404(titular_id)
    client.name = data['name']
    client.email = data['email']
    client.telefone = data['telefone']
    db.session.commit()
    return client.to_dict()

def delete_client(titular_id):
    client = Titular.query.get_or_404(titular_id)
    db.session.delete(client)
    db.session.commit()
    return '', 204

def client_next_id():
    ids_existentes = (
        Titular.query.with_entities(Titular.numero_dizimista)
        .order_by(Titular.numero_dizimista)
        .all()
    )
    ids_usados = set(id[0] for id in ids_existentes)

    for i in range(1, 10000):
        if i not in ids_usados:
            return i