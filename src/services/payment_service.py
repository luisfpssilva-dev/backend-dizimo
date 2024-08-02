from src.models.pagamento_model import Payment
from src.models.titular_model import TitularModel
from src.models.usuario_model import User
from src.db import db

def get_all_payments():
    return [payment.to_dict() for payment in Payment.query.all()]

def get_payment_by_id(payment_id):
    payment = Payment.query.get(payment_id)
    if payment:
        return payment.to_dict()
    else:
        return None

def create_payment(data):
    client = TitularModel.query.get(data['client_id'])
    user = User.query.get(data['user_id'])
    if not client or not user:
        raise ValueError('Client or User not found')

    payment = Payment(
        amount=data['amount'],
        description=data.get('description'),
        client_id=data['client_id'],
        user_id=data['user_id']
    )
    db.session.add(payment)
    db.session.commit()
    return payment.to_dict()

def update_payment(payment_id, data):
    payment = Payment.query.get(payment_id)
    if payment:
        payment.amount = data['amount']
        payment.description = data.get('description')
        payment.client_id = data['client_id']
        payment.user_id = data['user_id']
        db.session.commit()
        return payment.to_dict()
    else:
        return None

def delete_payment(payment_id):
    payment = Payment.query.get(payment_id)
    if payment:
        db.session.delete(payment)
        db.session.commit()
        return True
    else:
        return False
