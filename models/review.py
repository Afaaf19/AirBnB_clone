#!/usr/bin/python3
"""Class review"""

from models.base_model import BaseModel


class Review(BaseModel):
    """class that inherits from BaseModel,
       defines reviews made by users"""
    place_id = ""
    user_id = ""
    text = ""
