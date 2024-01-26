#!/usr/bin/python3
"""
Starts a Flask web application that listens on 0.0.0.0, port 5000
"""
from flask import Flask


app = Flask(__name__)

@app.route("/", strict_slashes=False)
def Hello_HBNB():
    """
    Returns: Hello HBNB string.
    """ 
    return "<p>Hello HBNB!</p>"


    if __name__ == "__main__":
        app.run(host='0.0.0.0', port=5000)
