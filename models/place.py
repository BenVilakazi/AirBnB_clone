#!/usr/bin/python3
"""Class Place Inherits from BaseModel"""

import models

class Place(models.BaseModel):
    """Class to Store place information"""
    city_id = ""
    user_id = ""
    name = ""
    descrption = ""
    number_rooms = 0
    number_bathrooms = 0
    max_guest = 0
    price_by_night = 0
    longitude = 0.0
    latitude = 0.0
    amnenity_ids = []