# src/models/pagamento_model.py
from src.db import db
from datetime import datetime

class Payment(db.Model):
    __tablename__ = 'payments'
    __table_args__ = {'extend_existing': True}

    id = db.Column(db.Integer, primary_key=True)
    amount = db.Column(db.Float, nullable=False)
    date = db.Column(db.DateTime, default=datetime.utcnow)
    titular_id = db.Column(db.String(32), db.ForeignKey('titular.titular_id'), nullable=False)
    user_id = db.Column(db.Integer, db.ForeignKey('users.id'), nullable=False)

    def to_dict(self):
        return {
            'id': self.id,
            'amount': self.amount,
            'date': self.date,
            'titular_id': self.titular_id,
            'user_id': self.user_id
        }
