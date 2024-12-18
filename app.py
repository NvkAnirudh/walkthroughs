from flask import Flask
from flask_jwt_extended import JWTManager
from routes import auth_bp
from database import db, init_db
from dotenv import load_dotenv
import os

# Load environment variables
load_dotenv()

app = Flask(__name__)

# Application Configuration
app.config['SQLALCHEMY_DATABASE_URI'] = os.getenv('DATABASE_URL')
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['JWT_SECRET_KEY'] = os.getenv('JWT_SECRET_KEY')

# Initialize database and JWT
db.init_app(app)
jwt = JWTManager(app)

