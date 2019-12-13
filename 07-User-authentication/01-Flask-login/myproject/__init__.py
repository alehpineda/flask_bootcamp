# __init__.py

from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask_login import LoginManager

login_manager = LoginManager()

app = Flask(__name__)

app.config['SECRET_KEY'] = 'MYSECRETEKEY'

# SQL database config
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql+psycopg2://flask:flask@localhost:5432/flask_login_dev'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)
Migrate(app, db)

# Login config
login_manager.init_app(app)
login_manager.login_view = 'login' # must equal the view
