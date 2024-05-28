#!/usr/bin/python3
"""import libraries"""
from flask import Flask, render_template
from models.state import State
from models import storage
from models import *
# import sys

# sys.path.append('..')

# from models import storage
# from models.state import State
# from models import *


hbnb = Flask(__name__)


@hbnb.route("/states_list", strict_slashes=False)
def states_list():
    states = sorted(list(storage.all(State).values()), key=lambda x: x.name)
    return render_template("7-states_list.html", states=states)


@hbnb.route("//cities_by_states", strict_slashes=False)
def cities_by_states():
    states = storage.all(State).values()
    return render_template("8-cities_by_states.html", states=states)


@hbnb.teardown_appcontext
def close_session(exception):
    storage.close()


if __name__ == "__main__":
    hbnb.run(debug=True, host="0.0.0.0", port=5000)
