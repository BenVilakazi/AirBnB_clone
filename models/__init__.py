#!/usr/bin/python3
"""Import FleStorage and Read existing data into `storage` variable"""

from models.engine.file_storage import FileStorage 
from models.base_model import BaseModel
from models.state import State
from models.city import City
from models.place import Place
from models.amenity import Amenity
from models.review import Review
from models.user import User

class_dict = {
    'BaseModel': BaseModel,
    'State': State,
    'City' : City,
    'Place' : Place,
    'Amenity' : Amenity,
    'Review' : Review,
    'User' : User
}

storage = FileStorage()
storage.reload()