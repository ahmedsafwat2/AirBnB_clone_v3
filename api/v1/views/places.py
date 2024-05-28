#!/usr/bin/python3
"""module for places routes
"""
from api.v1.views import app_views
from models import storage
from flask import jsonify, abort, request
from models.all_models import our_models
from models.place import Place
from models.city import City


@app_views.route('/cities/<city_id>/places/', methods=['GET'])
@app_views.route('/cities/<city_id>/places', methods=['GET'])
def get_places(city_id):
    """return json format for places object
    """
    places_list = []
    for item in storage.all(Place).values():
        dict_item = item.to_dict()
        if dict_item['city_id'] == city_id:
            places_list.append(dict_item)
    if places_list == []:
        abort(404)
    return jsonify(places_list)


@app_views.route("/places/<place_id>/", methods=['GET'])
@app_views.route("/places/<place_id>", methods=['GET'])
def get_places_id(place_id):
    """get json format for specific id
    """
    place = storage.get(Place, place_id)
    if place is None:
        abort(404)
    return jsonify(place.to_dict())


@app_views.route("/places/<place_id>/", methods=['DELETE'])
@app_views.route("/places/<place_id>", methods=['DELETE'])
def delete_places_id(place_id):
    """delete city object based on id
    """
    place = storage.get(Place, place_id)
    if place is None:
        abort(404)
    else:
        storage.delete(place)
        storage.save()
        return jsonify({}), 200


@app_views.route("/cities/<city_id>/places/", methods=['POST'])
@app_views.route("/cities/<city_id>/places", methods=['POST'])
def post_places(city_id):
    """create new place object
    """
    city = storage.get(City, city_id)
    if city is None:
        abort(404)
    if not request.get_json():
        abort(400, "Not a JSON")
    if 'name' not in request.get_json():
        abort(400, "Missing user_id")
    if 'user_id' not in request.get_json():
        abort(400, "Missing name")

    place = Place(
        name=request.json['name'], city_id=city_id,
        user_id=request.json['user_id'])
    storage.new(place)
    storage.save()
    return (jsonify(place.to_dict())), 201


@app_views.route("/places/<place_id>/", methods=['PUT'])
@app_views.route("/places/<place_id>", methods=['PUT'])
def update_places(place_id):
    """create new name for place object
    """
    args = ["name", "description", "number_rooms",
            "number_bathrooms", "max_guest",
            "price_by_night", "latitude",
            "longitude", "amenity_ids"]
    if not request.get_json():
        abort(400, "Not a JSON")
    # json_data = request.get_json()
    place = storage.get(Place, place_id)
    if place is None:
        abort(404)
    for attr in args:
        if attr in request.get_json():
            setattr(place, attr, request.json[attr])
    storage.save()
    return jsonify(place.to_dict()), 200
