#!/usr/bin/python3
"""Store first obj"""

import models
import json

def models_obj_hook(o_dict):
    """Import BaseModel from models and returms dict"""
    try:
        cls = o_dict['__class__']
    except KeyError:
        return o_dict
    else:
        try:
            return getattr(models, cls)(**o_dict)
        except AttributeError:
            return o_dict
        
class FileStorage:
    """created private class attr"""
    __file_path = "file.json"
    __objects = {}
    
def all(self):
    pass

def new(self):
    pass

def save(self):
    pass

def reload(self):
    pass