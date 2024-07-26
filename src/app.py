import os
import sys
from flask import Flask
from flask_restful import Api
from flask_cors import CORS
from dotenv import load_dotenv
from flask_jwt_extended import JWTManager

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

load_dotenv() 
app = Flask(__name__)
jwt = JWTManager(app)
app.config['SECRET_KEY'] = os.getenv('SECRET_KEY', 'lmi')
app.config['SQLALCHEMY_DATABASE_URI'] = os.getenv('DATABASE_URL', 'sqlite:///dizimo.db')
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['JWT_SECRET_KEY'] = os.getenv('JWT_SECRET_KEY', 'your_jwt_secret_key')
cors = CORS(app, resources={r"/*": {"origins": "http://localhost:3000"}})
from src.db import db
db.init_app(app)

api = Api(app)

from routes.titular_routes import initialize_routes_titular
from routes.comunidade_route import initialize_routes_comunidade
from routes.user_route import initialize_user_routes
from src.routes.protected_route import initialize_protected_routes
initialize_protected_routes(api)
initialize_routes_comunidade(api)
initialize_routes_titular(api)
initialize_user_routes(api)

with app.app_context():
    db.create_all()

if __name__ == '__main__':
    app.run(debug=True,port=5002)
