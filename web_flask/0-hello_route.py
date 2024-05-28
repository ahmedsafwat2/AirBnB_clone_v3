#!/usr/bin/python3
"""import libraries"""
from flask import Flask

hbnb = Flask(__name__)


@hbnb.route("/", strict_slashes=False)
def homepage():
    """Home page"""
    return "Hello HBNB!"


if __name__ == "__main__":
    hbnb.run(debug=True, host="0.0.0.0", port=5000)
