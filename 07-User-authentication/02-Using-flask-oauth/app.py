from flask import Flask, url_for, render_template
from flask_dance.contrib.google import make_google_blueprint, google
# set env variables for local dev
import os
os.environ['OAUTHLIB_INSECURE_TRANSPORT'] = '1'
os.environ['OAUTHLIB_RELAX_TOKEN_SCOPE'] = '1'
################################################

app = Flask(__name__)

app.config['SECRET_KEY'] = 'mysupersecretkey'

client_id = ''  # fill with cliend id
client_secret = ''  # fill with client secret
g_bp = make_google_blueprint(client_id=client_id, client_secret=client_secret,
                             offline=True, scope=['profile', 'email'])

app.register_blueprint(g_bp, url_prefix='/login')

# views

# Home
@app.route('/')
def home():
    return render_template('home.html')

# welcome
@app.route('/welcome')
def welcome():
    resp = google.get('/oauth2/v2/userinfo')
    assert resp.ok, resp.text
    email = resp.json()['email']

    return render_template('welcome.html', email=email)

# login google
@app.route('/login/google')
def login():
    if not google.authorized:
        return render_template(url_for('google.login'))
    resp = google.get('/oauth2/v2/userinfo')
    assert resp.ok, resp.text
    email = resp.json()['email']
    response = resp.json()

    # redirect doesn't work cuz we need the variable in the context
    # of the template
    return render_template('welcome.html', email=email, response=response)


if __name__ == "__main__":
    app.run(debug=True, host='0.0.0.0')
