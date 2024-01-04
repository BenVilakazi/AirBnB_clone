#!/usr/bin/python3
"""BaseModel Class"""

import models
import uuid
from datetime import datetime

class BaseModel:
    """BaseModel class will be inherited by other classes"""
    def __init__(self, *args, **kwargs):
        """__init__ method & instantiation of class BaseModel"""
        self.id = str(uuid.uuid4())
        self.created_at = datetime.now()
        self.updated_at = self.created_at
        for name, value in kwargs.items():
            """searches through dict for keys"""
            if name == "__class__":
                continue
            setattr(self, name, value)
        if "id" not in kwargs:
            models.storage.new(self)
            
    def __setattr__(self, name, value):
        pass
    
    def __str__(self):
        """Format `self` for output"""
        pass
    
    def save(self):
        """Updates the public instance attr updated_at"""
        pass
    
    def to_dict(self):
        """Returns a Dictionary containing all key/value pairs of __dict__"""
        pass