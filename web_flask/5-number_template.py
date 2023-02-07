#!/usr/bin/python3
"""A script that starts a Flask application"""


from flask import Flask
from flask import render_template


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
def c(text):
    """Displays C and replaces _ with a space"""

    text = text.replace('_', ' ')
    return "C {}".format(text)


@app.route("/python/<text>", strict_slashes=False)
def python(text="is cool"):
    """Displays Python and the value of the variable"""

    text = text.replace('_', ' ')
    return "Python {}".format(text)


@app.route("/number/<int:n>", strict_slashes=False)
def number(n):
    """Displays m is a nmber if n is an integer"""

    if n == isinstance(n, int):
        return "{} is a number".format(n)

@app.route("/number_template/<int:n>", strict_slashs=False)
def number_template(n):
    """Return an integer n"""

    return render_template('5-number.html', n=n)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
