#!/usr/bin/python3
"""class User that inherits from BaseModel """

import models

class User(models.BaseModel):
    """class User """
    
    email = ""
    password = ""
    first_name = ""
    last_name = ""