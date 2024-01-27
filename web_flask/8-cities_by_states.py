#!/usr/bin/python3
"""
Starts a Flask web application that listens on 0.0.0.0, port 5000
"""
from flask import Flask, render_template
from models import storage
from models.state import State

app = Flask(__name__)


@app.teardown_appcontext
def teardown(exception):
    """
    Remove the current SQLAlchemy Session after each request
    """
    storage.close()


@app.route("/cities_by_states", strict_slashes=False)
def cities_by_states():
    """
    Display a HTML page with a list of all State objects sorted by name
    """
    sorted_states = sorted(storage.all(State).values(), key=lambda x: x.name)
    return render_template('8-cities_by_states.html', states=sorted_states)


if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000)
