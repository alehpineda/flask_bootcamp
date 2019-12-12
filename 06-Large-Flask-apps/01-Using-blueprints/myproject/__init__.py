# __init__.py initialization of the project

from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate


app = Flask(__name__)

app.config['SECRET_KEY'] = 'SECRETKEY'

# SQL database section
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql+psycopg2://flask:flask@db:5432/puppies_dev'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)
Migrate(app, db)

# Needs to be after the db registration
# else raise an error
from myproject.puppies.views import puppies_bp
from myproject.owners.views import owners_bp


app.register_blueprint(owners_bp, url_prefix='/owners')
app.register_blueprint(puppies_bp, url_prefix='/puppies')
