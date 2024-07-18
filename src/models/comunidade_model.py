from src.db import db
from src.utils.utils import generate_uuid
from sqlalchemy.ext.declarative import declarative_base


Base = declarative_base()
metadata = Base.metadata

class ComunidadeModel(Base):
    __tablename__ = 'comunidade'
    comunidade_id = db.Column(db.String(32), primary_key=True, default=generate_uuid)
    nome = db.Column(db.String(80), nullable=False)
    updated_at = db.Column(db.DateTime)


    def to_dict(self):
        return {
            'comunidade_id': self.comunidade_id,
            'nome': self.nome
        }
