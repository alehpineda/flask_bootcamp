from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def index():
    some_variable = 'Alex'
    letters = list(some_variable)
    return render_template('basic.html', my_variable=some_variable, letters=letters)

if __name__ == "__main__":
    app.run(debug=True)
