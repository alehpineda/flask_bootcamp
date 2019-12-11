# Owners --> forms.py

from flask_wtf import FlaskForm
from wtforms import StringField, IntegerField, SubmitField


class AddForm(FlaskForm):
    name = StringField('Name of owner: ')
    puppy_id = IntegerField('ID of the puppy to adopt : ')
    submit = SubmitField('Add Owner')
