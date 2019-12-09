from flask import Flask, render_template
# Imports for the forms
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField

app = Flask(__name__)

# config secret key
app.config['SECRET_KEY'] = 'my_super_secret_key'

# declare form class
class InfoForm(FlaskForm):

    breed = StringField('What Breed are you?')
    submit = SubmitField('Submit')


# route with methods get and post
@app.route('/', methods=['GET', 'POST'])
def index():
    breed = False
    #instanciate the form
    form = InfoForm()
    # validate the form
    if form.validate_on_submit():
        # get data from form
        breed = form.breed.data
        # clear the field form
        form.breed.data = ''
    
    # pass the form and variable to the template
    return render_template('index.html', form=form, breed=breed)


if __name__ == "__main__":
    app.run(debug=True)
