#!/usr/bin/python3
"""import libraries"""
from flask import Flask

hbnb = Flask(__name__)


@hbnb.route("/", strict_slashes=False)
def homepage():
    """Home page"""
    return "Hello HBNB!"


@hbnb.route("/hbnb", strict_slashes=False)
def hbnbpage():
    """HBNB page"""
    return "HBNB"


@hbnb.route("/c/<text>", strict_slashes=False)
def cpage(text):
    """C page"""
    text = text.replace("_", " ")
    return f"C {text}"


if __name__ == "__main__":
    hbnb.run(debug=True, host="0.0.0.0", port=5000)
