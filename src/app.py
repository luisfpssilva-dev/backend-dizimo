import os
import sys
from flask import Flask
from flask_restful import Api
from flask_cors import CORS
from dotenv import load_dotenv

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

load_dotenv() 

app = Flask(__name__)
app.config['SECRET_KEY'] = os.getenv('SECRET_KEY', 'lmi')
app.config['SQLALCHEMY_DATABASE_URI'] = os.getenv('DATABASE_URL', 'sqlite:///dizimo.db')
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False 
CORS(app)
from src.db import db
db.init_app(app)

api = Api(app)

from routes.titular_routes import initialize_routes_titular
from routes.comunidade_route import initialize_routes_comunidade
initialize_routes_comunidade(api)
initialize_routes_titular(api)

with app.app_context():
    db.create_all()

if __name__ == '__main__':
    app.run(debug=True,port=5002)
