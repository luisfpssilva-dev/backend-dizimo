from src.models.usuario_model import User
from src.db import db
from werkzeug.security import generate_password_hash, check_password_hash

def create_user(data):
    if User.query.filter_by(username=data['username']).first():
        raise ValueError('Username already exists')
    
    new_user = User(username=data['username'])
    new_user.set_password(data['password'])
    db.session.add(new_user)
    db.session.commit()
    return new_user.to_dict()

def authenticate_user(username, password):
    user = User.query.filter_by(username=username).first()
    if user and user.check_password(password):
        return user.to_dict()
    else:
        raise ValueError('Invalid username or password')
