#!/usr/bin/python3
"""Define a class named 'city'"""
from models.base_model import BaseModel


class City(BaseModel):
    """Inherits from the basemodel"""
    state_id = ""
    name = ""
