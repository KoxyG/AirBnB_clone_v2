#!/usr/bin/python3
"""A script that starts a Flask application"""


from flask import Flask


app = Flask(__name__)


@app.route("/", strict_slashes=False)
def hello_hbnb():
    """Displays HBNB!"""
    return "Hello HBNB!"

@app.route("/hbnb", strict_slashes=False)
def hbnb():
    """Displays HBNB"""
    return "HBNB"

@app.route("/c/<text>", strict_slashes=False)
def c_text():
    """Displays C"""
    text = text.replace('_', ' ')
    return "C {}".format(text)


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
