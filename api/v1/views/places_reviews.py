#!/usr/bin/python3
"""module for places routes
"""
from api.v1.views import app_views
from models import storage
from flask import jsonify, abort, request
from models.all_models import our_models
from models.place import Place
from models.review import Review
from models.user import User


@app_views.route('/places/<place_id>/reviews', methods=['GET'])
@app_views.route('/places/<place_id>/reviews', methods=['GET'])
def get_reviews(place_id):
    """list of all Review objects of a Place
    """
    place_object = storage.get(Place, place_id)
    if place_object is None:
        abort(404)
    review_list = []
    for item in storage.all(Review).values():
        dict_item = item.to_dict()
        if dict_item['place_id'] == place_id:
            review_list.append(dict_item)
    if review_list == []:
        abort(404)
    return jsonify(review_list)


@app_views.route("/reviews/<review_id>/", methods=['GET'])
@app_views.route("/reviews/<review_id>", methods=['GET'])
def get_review_id(review_id):
    """Review object
    """
    review = storage.get(Review, review_id)
    if review is None:
        abort(404)
    return jsonify(review.to_dict())


@app_views.route("/reviews/<review_id>/", methods=['DELETE'])
@app_views.route("/reviews/<review_id>", methods=['DELETE'])
def delete_review_id(review_id):
    """delete review object based on id
    """
    review = storage.get(Review, review_id)
    if review is None:
        abort(404)
    else:
        storage.delete(review)
        storage.save()
        return jsonify({}), 200


@app_views.route("/places/<place_id>/reviews/", methods=['POST'])
@app_views.route("/places/<place_id>/reviews", methods=['POST'])
def post_review(place_id):
    """create new review object
    """
    place = storage.get(Place, place_id)
    if place is None:
        abort(404)
    if not request.get_json():
        abort(400, "Not a JSON")
    if 'user_id' not in request.get_json():
        abort(400, "Missing user_id")
    if 'user_id' not in request.get_json():
        abort(400, "Missing name")
    user = storage.get(User, request.json['user_id'])
    if user is None:
        abort(404)
    if 'text' not in request.get_json():
        abort(400, 'Missing text')

    review = Review(
        text=request.json['text'], place_id=place_id,
        user_id=request.json['user_id'])
    storage.new(review)
    storage.save()
    return (jsonify(review.to_dict())), 201


@app_views.route("/reviews/<review_id>/", methods=['PUT'])
@app_views.route("/reviews/<review_id>", methods=['PUT'])
def update_reviews(review_id):
    """create new name for place object
    """
    if not request.get_json():
        abort(400, "Not a JSON")
    # json_data = request.get_json()
    review = storage.get(Review, review_id)
    if review is None:
        abort(404)

    if "text" in request.get_json():
        setattr(review, 'text', request.json['text'])
    storage.save()
    return jsonify(review.to_dict()), 200
