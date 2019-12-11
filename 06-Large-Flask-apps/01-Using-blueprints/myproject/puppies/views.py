# puppies --> views
from flask import Blueprint, render_template, redirect, url_for
from myproject import db
from myproject.models import Puppy
from myproject.puppies.forms import AddForm, DelForm


# Blueprints
puppies_bp = Blueprint('puppies', __name__, template_folder='templates/puppies')

# add new puppy
@puppies_bp.route('/add', methods=['GET', 'POST'])
def add_pup():

    form = AddForm()

    # add new puppy to the db
    if form.validate_on_submit():
        name = form.name.data

        new_pup = Puppy(name)
        db.session.add(new_pup)
        db.session.commit()

        return redirect(url_for('puppies.list_pup'))

    return render_template('add.html', form=form)


# list of puppies
@puppies_bp.route('/list')
def list_pup():

    puppies = Puppy.query.all()
    return render_template('list.html', puppies=puppies)


# a puppy was adopted and taken home
@puppies_bp.route('/delete', methods=['GET', 'POST'])
def del_pup():

    form = DelForm()

    if form.validate_on_submit():
        id = form.id.data

        pup = Puppy.query.get(id)
        db.session.delete(pup)
        db.session.commit()

        return redirect(url_for('puppies.list_pup'))
    return render_template('delete.html', form=form)
