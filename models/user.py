#!/usr/bin/python3
"""The User class"""
from models.base_model import BaseModel


class User(BaseModel):
    """User class is a child class from base class-BaseModel"""
    email = ""
    password = ""
    first_name = ""
    last_name = ""
