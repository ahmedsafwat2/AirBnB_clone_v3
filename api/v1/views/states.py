#!/usr/bin/python3
"""module for states routes
"""
from api.v1.views import app_views
from models import storage
from flask import jsonify, abort, request
from models.all_models import our_models
from models.state import State


@app_views.route('/states', methods=['GET'])
def get_states():
    """return json format for states object
    """
    states_list = []
    for item in storage.all(State).values():
        states_list.append(item.to_dict())
    return jsonify(states_list)


@app_views.route("/states/<state_id>", methods=['GET'])
def get_states_id(state_id):
    """get json format for specific id
    """
    state = storage.get(State, state_id)
    if state is None:
        abort(404)
    return jsonify(state.to_dict())


@app_views.route("/states/<state_id>", methods=['DELETE'])
def delete_states_id(state_id):
    """delete state object based on id
    """
    state = storage.get(State, state_id)
    if state is None:
        abort(404)
    else:
        storage.delete(state)
        storage.save()
        return jsonify({}), 200


@app_views.route("/states/", methods=['POST'])
def post_states():
    """create new state object
    """
    if not request.get_json():
        abort(400, "Not a JSON")
        # raise NotFound(description="Missing name")
    # json_data = request.get_json()
    if 'name' not in request.get_json():
        abort(400, "Missing name")
        # raise NotFound(description="Missing name")
    state = State(name=request.json['name'])
    # state = State(name=json_data['name'])
    storage.new(state)
    storage.save()
    return (jsonify(state.to_dict())), 201


@app_views.route("/states/<state_id>", methods=['PUT'])
def update_states(state_id):
    """create new name for state object
    """
    if not request.get_json():
        abort(400, "Not a JSON")
    # json_data = request.get_json()
    state = storage.get(State, state_id)
    if state is None:
        abort(404)
    setattr(state, "name", request.json['name'])
    storage.save()
    return jsonify(state.to_dict()), 200
