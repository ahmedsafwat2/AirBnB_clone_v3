#!/usr/bin/python3
"""module for users routes"""
from api.v1.views import app_views
from models import storage
from flask import jsonify, abort, request
from models.user import User


@app_views.route('/users', methods=['GET'])
def get_users():
    """return json format for users object
    """
    users_list = []
    for item in storage.all(User).values():
        users_list.append(item.to_dict())
    return jsonify(users_list)


@app_views.route("/users/<user_id>", methods=['GET'])
def get_users_id(user_id):
    """get json format for specific id
    """
    user = storage.get(User, user_id)
    if user is None:
        abort(404)
    return jsonify(user.to_dict())


@app_views.route("/users/<user_id>", methods=['DELETE'])
def delete_users_id(user_id):
    """delete user object based on id
    """
    user = storage.get(User, user_id)
    if user is None:
        abort(404)
    else:
        storage.delete(user)
        storage.save()
        return jsonify({}), 200


@app_views.route("/users", methods=['POST'])
def post_users():
    """create new user object
    """
    if not request.get_json():
        abort(400, "Not a JSON")
        # raise NotFound(description="Missing name")
    # json_data = request.get_json()
    if 'email' not in request.get_json():
        abort(400, "Missing email")
    if 'password' not in request.get_json():
        abort(400, "Missing password")
    user = User(email=request.json['email'], password=request.json['password'])
    storage.new(user)
    storage.save()
    return (jsonify(user.to_dict())), 201


@app_views.route("/users/<user_id>", methods=['PUT'])
def update_users(user_id):
    """create new name for user object
    """
    if not request.get_json():
        abort(400, "Not a JSON")
    # json_data = request.get_json()
    user = storage.get(User, user_id)
    if user is None:
        abort(404)
    if "first_name" in request.get_json():
        setattr(user, "first_name", request.json['first_name'])
    if "last_name" in request.get_json():
        setattr(user, "last_name", request.json['last_name'])
    if "password" in request.get_json():
        setattr(user, "password", request.json['password'])
    storage.save()
    return jsonify(user.to_dict()), 200
