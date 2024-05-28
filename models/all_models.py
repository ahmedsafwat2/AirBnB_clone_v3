#!/usr/bin/python3

from models.base_model import BaseModel
from models.user import User
from models.city import City
from models.state import State
from models.place import Place
from models.review import Review
from models.amenity import Amenity

our_models = {
    "BaseModel":  BaseModel,
    "User": User,
    "City": City,
    "State": State,
    "Place": Place,
    "Review": Review,
    "Amenity": Amenity
}
