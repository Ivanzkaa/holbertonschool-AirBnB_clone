#!/usr/bin/python3
"""Define a class named 'review'"""
from models.base_model import BaseModel


class Review(BaseModel):
    """Inherits from the basemodel"""
    place_id = ""
    user_id = ""
    text = ""
