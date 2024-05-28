#!/usr/bin/python3
"""import libraries"""
from flask import Flask, Blueprint, jsonify
from os import getenv, environ
from models import storage
from api.v1.views import app_views
from flask import make_response
from flask_cors import CORS


app = Flask(__name__)
CORS(app, resources={r"/api/*": {"origins": "0.0.0.0"}})

app.url_map.strict_slashes = False
app.register_blueprint(app_views)


@app.teardown_appcontext
def close_session(exception):
    """close session"""
    storage.close()


@app.errorhandler(404)
def not_found(error):
    return make_response(jsonify({"error": "Not found"}), 404)


if __name__ == '__main__':
    # if getenv("HBNB_API_HOST") is None:
    #     HBNB_API_HOST = '0.0.0.0'
    # else:
    #     HBNB_API_HOST = getenv("HBNB_API_HOST")
    # if getenv("HBNB_API_PORT") is None:
    #     HBNB_API_PORT = 5000
    # else:
    #     HBNB_API_PORT = int(getenv("HBNB_API_PORT"))
    if environ.get("HBNB_API_HOST") is None:
        HBNB_API_HOST = '0.0.0.0'
    else:
        HBNB_API_HOST = environ.get("HBNB_API_HOST")
    if environ.get("HBNB_API_PORT") is None:
        HBNB_API_PORT = 5000
    else:
        HBNB_API_PORT = int(environ.get("HBNB_API_PORT"))
    app.run(debug=True, host=HBNB_API_HOST, port=HBNB_API_PORT, threaded=True)
