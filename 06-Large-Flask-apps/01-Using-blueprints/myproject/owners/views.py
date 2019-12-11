# owners --> views

from flask import Blueprint, render_template, redirect, url_for
from myproject import db
from myproject.models import Owner
from myproject.owners.forms import AddForm

owners_bp = Blueprint('owners', __name__, template_folder='templates/owners')


# add owner for adopted puppy
@owners_bp.route('/add', methods=['GET', 'POST'])
def add_owner():

    form = AddForm()

    # add new puppy to the db
    if form.validate_on_submit():

        name = form.name.data
        puppy_id = form.puppy_id.data

        new_owner = Owner(name, puppy_id)
        db.session.add(new_owner)
        db.session.commit()

        # puppies.list references the template
        return redirect(url_for('puppies.list_pup'))

    return render_template('add_owner.html', form=form)
