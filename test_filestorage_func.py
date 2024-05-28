#!/usr/bin/python3
from models import storage
from models.base_model import BaseModel
from models.engine import file_storage

f = file_storage.FileStorage()
print(f.all())
print(type(f.all()))
