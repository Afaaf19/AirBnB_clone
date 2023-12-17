#!/usr/bin/python3
"""Class city"""

from models.base_model import BaseModel


class City(BaseModel):
    """Class that inherits from BaseModel, it defines attributes"""
    state_id = ""
    name = ""
