# forms.py

from flask_wtf import FlaskForm
from wtforms import StringField, IntegerField, SubmitField


class AddForm(FlaskForm):

    name = StringField('Name of Puppy: ')
    submit = SubmitField('Add Puppy')


class DelForm(FlaskForm):

    id = IntegerField('Id Number of Puppy to remove: ')
    submit = SubmitField('Remove Puppy')


class AddOwnerForm(FlaskForm):
    name = StringField('Name of owner: ')
    puppy_id = StringField('ID of the puppy to adopt : ')
    submit = SubmitField('Add Owner')
