from datetime import datetime
from src.db import db
from src.utils.utils import generate_uuid


class TitularModel(db.Model):
    __tablename__ = 'titular'
    __table_args__ = {'extend_existing': True}

    titular_id = db.Column(db.String(32), primary_key=True)
    name = db.Column(db.String(80), nullable=False)
    comunidade_id = db.Column(db.String(32), db.ForeignKey('comunidade.comunidade_id'), nullable=False)
    user_id = db.Column(db.Integer, db.ForeignKey('users.id'), nullable=False)

    user = db.relationship('User', back_populates='titulares')
    comunidade_relation = db.relationship('ComunidadeModel', back_populates='titulares')
    payments = db.relationship('Payment', back_populates='titular', lazy=True)

    def to_dict(self):
        return {
            'titular_id': self.titular_id,
            'name': self.name,
            'comunidade_id': self.comunidade_id,
            'user_id': self.user_id
        }



class EnderecoModel(db.Model):
    __tablename__ = 'endereco'
    __table_args__ = {'extend_existing': True}

    endereco_id = db.Column(db.String(32), primary_key=True, default=generate_uuid)
    titular_id = db.Column(db.String(32), db.ForeignKey('titular.titular_id'))
    cep = db.Column(db.String(32), nullable=False)
    rua = db.Column(db.String(32), nullable=False)
    numero = db.Column(db.String(10), nullable=False)
    bairro = db.Column(db.String(32), nullable=False)
    cidade = db.Column(db.String(32), nullable=False)
    complemento = db.Column(db.String(32), nullable=False)
    updated_at = db.Column(db.DateTime, default=datetime.now, onupdate=datetime.now)

    titular_relation = db.relationship('TitularModel', back_populates='enderecos')

    def to_dict(self):
        return {
            'endereco_id': self.endereco_id,
            'titular_id': self.titular_id,
            'cep': self.cep,
            'rua': self.rua,
            'numero': self.numero,
            'bairro': self.bairro,
            'cidade': self.cidade,
            'complemento': self.complemento,
            'updated_at': self.updated_at,
            'titular_relation': self.titular_relation.to_dict() if self.titular_relation else None
        }
        
        
class DependenteModel(db.Model):
    __tablename__ = 'dependente'
    __table_args__ = {'extend_existing': True}

    dependente_id = db.Column(db.String(32), primary_key=True, default=generate_uuid)
    nome = db.Column(db.String(32), nullable=False)
    sexo = db.Column(db.String(32), nullable=False)
    titular_id = db.Column(db.String(32), db.ForeignKey('titular.titular_id'))
    tipo_dependente = db.Column(db.String(32), nullable=False)
    updated_at = db.Column(db.DateTime, default=datetime.now, onupdate=datetime.now)

    titular_relation = db.relationship('TitularModel', back_populates='dependentes')

    def to_dict(self):
        return {
            'dependente_id': self.dependente_id,
            'nome': self.nome,
            'sexo': self.sexo,
            'titular_id': self.titular_id,
            'tipo_dependente': self.tipo_dependente,
            'updated_at': self.updated_at,
            'titular_relation': self.titular_relation.to_dict() if self.titular_relation else None
        }