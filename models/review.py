#!/usr/bin/python3
"""class Review inherits from BaseModel"""

import models

class Review(models.BaseModel):
    """Class Reviews"""
    place_id = ""
    user_id = ""
    text = ""