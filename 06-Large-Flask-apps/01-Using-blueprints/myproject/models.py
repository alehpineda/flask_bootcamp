# models.py
# setup db object inside __init__.py initialization
# of the project
from myproject import db

###############
# DB Models ###
###############


class Puppy(db.Model):
    __tablename__ = 'puppies'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.Text)
    # one to one, a puppy can have one owner
    owner = db.relationship('Owner', backref='puppy', uselist=False)

    def __init__(self, name):
        self.name = name

    def __repr__(self):
        if self.owner:
            return f"Puppy name is {self.name} and owner is {self.owner.name}."
        else:
            return f"Puppy name is {self.name} and is ready for adoption!"


class Owner(db.Model):
    __tablename__ = 'owners'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.Text)

    puppy_id = db.Column(db.Integer, db.ForeignKey('puppies.id'))

    def __init__(self, name, puppy_id):
        self.name = name
        self.puppy_id = puppy_id

    def __repr__(self):
        return f"{self.name}"
