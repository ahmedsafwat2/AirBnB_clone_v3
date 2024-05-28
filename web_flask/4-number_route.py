#!/usr/bin/python3
"""import libraries"""
from flask import Flask, render_template

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


@hbnb.route("/python/", strict_slashes=False)
@hbnb.route("/python/<text>", strict_slashes=False)
def ptyhonpage(text="is cool"):
    """python page"""
    text = text.replace("_", " ")
    return f"Python {text}"


@hbnb.route("/number/<int:n>", strict_slashes=False)
def numberpage(n):
    """Number page"""
    return f"{n} is a number"


if __name__ == "__main__":
    hbnb.run(debug=True, host="0.0.0.0", port=5000)
