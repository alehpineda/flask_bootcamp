# adoption_site.py

from forms import AddForm, DelForm, AddOwnerForm
from flask import Flask, render_template, url_for, redirect
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate

app = Flask(__name__)

app.config['SECRET_KEY'] = 'SECRETKEY'

# SQL database section

# PostgreSQL Conection
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql+psycopg2://flask_bootcamp:flask_bootcamp@localhost:5432/flask_bootcamp_dev_puppies'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)
Migrate(app, db)

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

####################################
# View functions -- have forms     #
####################################

# home page
@app.route('/')
def index():
    return render_template('home.html')


# add new puppy
@app.route('/add', methods=['GET', 'POST'])
def add_pup():

    form = AddForm()

    # add new puppy to the db
    if form.validate_on_submit():
        name = form.name.data

        new_pup = Puppy(name)
        db.session.add(new_pup)
        db.session.commit()

        return redirect(url_for('list_pup'))

    return render_template('add.html', form=form)


# list of puppies
@app.route('/list')
def list_pup():

    puppies = Puppy.query.all()
    return render_template('list.html', puppies=puppies)


# a puppy was adopted and taken home
@app.route('/delete', methods=['GET', 'POST'])
def del_pup():

    form = DelForm()

    if form.validate_on_submit():
        id = form.id.data

        pup = Puppy.query.get(id)
        db.session.delete(pup)
        db.session.commit()

        return redirect(url_for('list_pup'))
    return render_template('delete.html', form=form)


# add owner for adopted puppy
@app.route('/add_owner', methods=['GET', 'POST'])
def add_owner():

    form = AddOwnerForm()

    # add new puppy to the db
    if form.validate_on_submit():

        name = form.name.data
        puppy_id = form.puppy_id.data

        new_owner = Owner(name, puppy_id)
        db.session.add(new_owner)
        db.session.commit()

        return redirect(url_for('list_pup'))

    return render_template('add_owner.html', form=form)


if __name__ == "__main__":
    app.run(debug=True)
