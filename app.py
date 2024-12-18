import os
import datetime
import secrets
from dotenv import load_dotenv
import psycopg2
from flask_mail import Mail, Message
from flask_cors import CORS
from flask import Flask, request, jsonify, session, redirect, url_for
from flask_sqlalchemy import SQLAlchemy
from flask_session import Session
from werkzeug.security import generate_password_hash, check_password_hash
from flask_login import LoginManager, UserMixin, login_user, logout_user, login_required, current_user

app = Flask(__name__)
CORS(app)
app.secret_key = os.urandom(24)

load_dotenv()

# Mail Configuration


