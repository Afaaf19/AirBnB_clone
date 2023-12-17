#!/usr/bin/python3
"""
User class
"""
from models.base_model import BaseModel


class User(BaseModel):
    """Class that inherits from BaseModel class, it defines attributes"""

    email = ""
    password = ""
    first_name = ""
    last_name = ""
