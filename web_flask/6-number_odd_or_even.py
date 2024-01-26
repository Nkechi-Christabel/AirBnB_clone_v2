#!/usr/bin/python3
"""
Starts a Flask web application that listens on 0.0.0.0, port 5000
"""
from flask import Flask, render_template

app = Flask(__name__)


@app.route("/", strict_slashes=False)
def hello_hbnb():
    """
    Display "Hello HBNB!"
    """
    return "Hello HBNB!"


@app.route("/hbnb", strict_slashes=False)
def hbnb():
    """
    Display "HBNB"
    """
    return "HBNB"


@app.route("/c/<text>", strict_slashes=False)
def c_text(text):
    """
    Display "C " followed by the value of the text variable
    (replace underscore _ symbols with a space)
    """
    return "C {}".format(text.replace('_', ' '))


@app.route("/python/", defaults={'text': 'is_cool'}, strict_slashes=False)
@app.route("/python/<text>", strict_slashes=False)
def python_text(text):
    """
    Display "Python " followed by the value of the text variable
    (replace underscore _ symbols with a space)
    """
    return "Python {}".format(text.replace('_', ' '))


@app.route("/number/<int:n>", strict_slashes=False)
def number(n):
    """
    Display "n is a number" only if n is an integer
    """
    return "{} is a number".format(n)


@app.route("/number_template/<int:n>", strict_slashes=False)
def number_template(n):
    """
    Display a HTML page only if n is an integer:
    """
    if isinstance(n, int):
        return render_template('number.html', number=n)
    else:
        return "Not Found", 404


@app.route("/number_odd_or_even/<int:n>", strict_slashes=False)
def number_odd_or_even(n):
    """
    Display a HTML page only if n is an integer:
    """
    if isinstance(n, int):
        return render_template('odd_or_even.html', number=n, odd_even="even"
                               if n % 2 == 0 else "odd")


if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000)
