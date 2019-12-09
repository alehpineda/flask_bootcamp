from flask import Flask

app = Flask(__name__)

@app.route('/')
def index():
    return "hello puppies"


@app.route('/information')
def info():
    return "Puppies are cute"


@app.route("/puppy/<name>")
def puppy(name):
    return f"This is a page for {name.upper()}"

if __name__ == "__main__":
    app.run()
    