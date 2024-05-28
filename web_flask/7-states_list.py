#!/usr/bin/python3
"""import libraries"""
from flask import Flask, render_template
# from models.state import State
# from models import storage
# from models import *
import sys

sys.path.append('..')

from models import storage
from models.state import State
from models import *


hbnb = Flask(__name__)


# @hbnb.route("/", strict_slashes=False)
# def homepage():
#     return ("Hello World")


@hbnb.route("/states_list", strict_slashes=False)
def stateslist():
    states = sorted(list(storage.all(State).values()), key=lambda x: x.name)
    return render_template("7-states_list.html", states=states)


@hbnb.teardown_appcontext
def close_session(exception):
    storage.close()


if __name__ == "__main__":
    hbnb.run(debug=True, host="0.0.0.0", port=5000)
