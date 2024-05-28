#!/usr/bin/python3
"""module for city routes
"""
from api.v1.views import app_views
from models import storage
from flask import jsonify, abort, request
from models.all_models import our_models
from models.city import City
from models.state import State


@app_views.route('/states/<state_id>/cities', methods=['GET'])
def get_cities(state_id):
    """return json format for cities object
    """
    cities_list = []
    state = storage.get(State, state_id)
    if state is None:
        abort(404)
    for item in storage.all(City).values():
        dict_item = item.to_dict()
        if dict_item['state_id'] == state_id:
            cities_list.append(dict_item)
    if cities_list is None:
        abort(404)
    return jsonify(cities_list)


@app_views.route("/cities/<city_id>", methods=['GET'])
def get_cities_id(city_id):
    """get json format for specific id
    """
    city = storage.get(City, city_id)
    if city is None:
        abort(404)
    return jsonify(city.to_dict())


@app_views.route("/cities/<city_id>", methods=['DELETE'])
def delete_cities_id(city_id):
    """delete city object based on id
    """
    city = storage.get(City, city_id)
    if city is None:
        abort(404)
    else:
        storage.delete(city)
        storage.save()
        return jsonify({}), 200


@app_views.route("states/<state_id>/cities", methods=['POST'])
def post_cities(state_id):
    """create new city object
    """
    state = storage.get(State, state_id)
    if state is None:
        abort(404)
    if not request.get_json():
        abort(400, "Not a JSON")
    if 'name' not in request.get_json():
        abort(400, "Missing name")

    city = City(name=request.json['name'], state_id=state_id)
    storage.new(city)
    storage.save()
    return (jsonify(city.to_dict())), 201


@app_views.route("/cities/<city_id>", methods=['PUT'])
def update_cities(city_id):
    """create new name for city object
    """
    if not request.get_json():
        abort(400, "Not a JSON")
    # json_data = request.get_json()
    city = storage.get(City, city_id)
    if city is None:
        abort(404)
    setattr(city, "name", request.json['name'])
    storage.save()
    return jsonify(city.to_dict()), 200
