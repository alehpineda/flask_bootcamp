from flask import Flask, render_template, request

app = Flask(__name__)

# Home page
@app.route('/')
def index():
    return render_template('index.html')


# report page
@app.route('/report')
def report():
    # name of puppy
    username = request.args.get('username')
    # username validations
    checks = username_validations(username)
    # render template with variables
    return render_template('report.html', VALIDATIONS=VALIDATIONS, checks = checks)


def username_validations(username):
    checks = []
    if not any(char.isupper() for char in username):
        checks.append(1)
    if not any(char.islower() for char in username):
        checks.append(2)
    if not username[-1].isdigit():
        checks.append(3)
    return checks

VALIDATIONS = {
    1:'Must have an upper case letter somewhere.',
    2:'Must have a lower case letter somewhere.',
    3:'Must have a number at the end.'
}

# 404 page
@app.errorhandler(404)
def page_not_found(e):
    return render_template('404.html'), 404

if __name__ == "__main__":
    app.run(debug=True)