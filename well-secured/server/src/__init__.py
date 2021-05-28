from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy_utils.functions import database_exists
from flask_wtf.csrf import CSRFProtect

import logging, os

logging.basicConfig(level=logging.DEBUG)

DATABASE_URI = 'postgresql://{0}:{1}@{2}:{3}/{4}'.format(
    os.environ.get('POSTGRES_USER') or 'admin',
    os.environ.get('POSTGRES_PASSWORD') or 'admin',
    'db',
    '5432',
    os.environ.get('POSTGRES_DB') or 'default'
)

app = Flask(__name__, template_folder="templates")
app.config['SECRET_KEY'] = 'extremely-secret-key'
app.config['SQLALCHEMY_DATABASE_URI'] = DATABASE_URI
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)
from .models import User, Question, Answer
db.create_all()

csrf = CSRFProtect()
csrf.init_app(app)

from .auth import auth as auth_blueprint
from .main import main as main_blueprint
app.register_blueprint(auth_blueprint)
app.register_blueprint(main_blueprint)


logging.debug('App initialized')

