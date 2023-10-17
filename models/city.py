#!/usr/bin/python3
"""
this module creates a sub class for Basemodel named, City
"""
from models.base_model import BaseModel


class City(BaseModel):
    """City Model inherits from the BaseModel
    """
    state_id = ""
    name = ""
