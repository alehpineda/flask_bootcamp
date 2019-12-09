from flask import Flask

app = Flask(__name__)

@app.route('/')
def index():
    return "hello puppies"


@app.route('/information')
def info():
    return "Puppies are cute"

if __name__ == "__main__":
    app.run()
    