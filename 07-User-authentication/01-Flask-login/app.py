from myproject import app, db
from flask import render_template, redirect, request, url_for, flash
from flask_login import login_user, login_required, logout_user
from myproject.models import User
from myproject.forms import LoginForm, RegistrationForm

# Views ###


# Home page
@app.route('/')
def home():
    return render_template('home.html')

# Welcome page
@app.route('/welcome')
@login_required
def welcome_user():
    return render_template('welcome.html')

# Logout
@app.route('/logout')
@login_required
def logout():
    logout_user()  # From flask_login
    flash('You logged out')
    return redirect(url_for('home'))

# Login
@app.route('/login', methods=['GET', 'POST'])
def login():

    form = LoginForm()

    if form.validate_on_submit():
        user = User.query.filter_by(email=form.email.data).first()

        if user.check_password(form.password.data) and user is not None:

            login_user(user)
            flash('Logged in Successfully!')
            # were flask saves the next page to move
            # if the user trys to enter a page were
            # login status is required
            next = request.args.get('next')

            # If next doesnt exist redirect
            if next is None or not next[0] == '/':
                next = url_for('welcome_user')

            return redirect(next)

    return render_template('login.html', form=form)


# register view
@app.route('/register', methods=['GET', 'POST'])
def register():
    form = RegistrationForm()

    if form.validate_on_submit():
        user = User(email=form.email.data,
                    username=form.username.data,
                    password=form.password.data)

        db.session.add(user)
        db.session.commit()
        flash('Thanks for registering')
        return redirect(url_for('login'))

    return render_template('register.html', form=form)


if __name__ == "__main__":
    app.run(debug=True, host='0.0.0.0')
