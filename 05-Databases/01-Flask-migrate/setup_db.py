import os
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate # pip install flask-migrate

# ENV variable
#os.environ['FLASK_APP'] = __file__

#grab the abs path to the source file
basedir = os.path.abspath(os.path.dirname(__file__))

app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///'+os.path.join(basedir, 'data.sqlite')
app.config['SQLALCHEMY_TRACK_MODIFIVATIONS'] = False

db = SQLAlchemy(app)

Migrate(app, db)

# Start DB

class Puppy(db.Model):
    # Manual table name choice
    __tablename__ = 'puppies'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.Text)
    age = db.Column(db.Integer)
    breed = db.Column(db.Text)

    def __init__(self, name, age, breed):
        self.name = name
        self.age = age
        self.breed = breed
    

    def __repr__(self):
        return f"Puppy {self.name} is {self.age} year/s old"
