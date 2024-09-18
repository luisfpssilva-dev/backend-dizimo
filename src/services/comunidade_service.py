from src.models import ComunidadeModel as Comunidade
from src.db import db

def get_all_comunidades():
    return [comunidade.to_dict() for comunidade in Comunidade.query.all()]

def get_comunidade_by_id(comunidade_id):
    comunidade = Comunidade.query.get_or_404(comunidade_id)
    return comunidade.to_dict()

def create_comunidade(data):
    new_comunidade = Comunidade(
        nome=data['nome']
    )
    db.session.add(new_comunidade)
    db.session.commit()
    return new_comunidade.to_dict()

def update_comunidade(comunidade_id, data):
    comunidade = Comunidade.query.get_or_404(comunidade_id)
    comunidade.nome = data['nome']
    comunidade.email = data['email']
    comunidade.telefone = data['telefone']
    db.session.commit()
    return comunidade.to_dict()

def delete_comunidade(comunidade_id):
    comunidade = Comunidade.query.get_or_404(comunidade_id)
    db.session.delete(comunidade)
    db.session.commit()
    return '', 204
