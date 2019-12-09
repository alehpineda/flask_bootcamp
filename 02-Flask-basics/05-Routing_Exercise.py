# Set up your imports here!
# import ...
from flask import Flask

app = Flask(__name__)


@app.route('/') # Fill this in!
def index():
    # Welcome Page
    # Create a generic welcome page.
    return "<h1>Welcome! Go to /puppy_latin/name to see your name in puppy latin!</h1>"

@app.route('/puppy_latin/<name>') # Fill this in!
def puppylatin(name):
    # This function will take in the name passed
    # and then use "puppy-latin" to convert it!
    if name[-1].lower() == 'y':
        lat_name = name[:-1] + 'iful'
    else:
        lat_name = name + 'y'
    # HINT: Use indexing and concatenation of strings
    # For Example: "hello"+" world" --> "hello world"
    return f"Hi {name}! Your puppy latin name is {lat_name}"

if __name__ == '__main__':
    # Fill me in!
    #app.run(debug=True) for debug mode
    app.run()
