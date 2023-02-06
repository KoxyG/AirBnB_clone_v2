#!/usr/bin/python3
"""A scripts that starts a Flask application"""


from flask import Flask

app = Flask(__name__)


@app.route('/', strict_slashes=False)
def hello_world():
    """A script that returns hello_world"""
    return "Hello HBNB"

@app.route('/hbnb', strict_slashes=False)
def hbnb():
    """Displays HBNH"""
    return "HBNB"


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
