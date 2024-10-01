from datetime import datetime
from src.db import db
from src.utils.utils import generate_uuid

class ComunidadeModel(db.Model):
    __tablename__ = 'comunidade'
    __table_args__ = {'extend_existing': True}

    comunidade_id = db.Column(db.String(32), primary_key=True, default=generate_uuid)
    nome = db.Column(db.String(80), nullable=False)
    updated_at = db.Column(db.DateTime, default=datetime.now)
    user_id = db.Column(db.Integer, db.ForeignKey('users.id'), nullable=False)
    users = db.relationship('User', back_populates='comunidade', lazy=True)
    titulares = db.relationship('TitularModel', back_populates='comunidade_relation', lazy=True)

    def to_dict(self):
        return {
            'comunidade_id': self.comunidade_id,
            'nome': self.nome,
            'updated_at': self.updated_at
        }
