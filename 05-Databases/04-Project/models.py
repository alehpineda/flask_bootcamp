###############
# DB Models ###
###############

# adoption_site.py
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate

app = Flask(__name__)

app.config['SECRET_KEY'] = 'SECRETKEY'

# SQL database section

# PostgreSQL Conection
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql+psycopg2://flask_bootcamp:flask_bootcamp@localhost:5432/flask_bootcamp_dev'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)
Migrate(app, db)


class Puppy(db.Model):
    __tablename__ = 'puppies'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.Text)

    def __init__(self, name):
        self.name = name

    def __repr__(self):
        return f"Puppy name: {self.name}"
