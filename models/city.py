#!/usr/bin/python3
"""
creates a sub class for Basemodel named, City
"""
from models.base_model import BaseModel


class City(BaseModel):
    """This file defines the City Model
    It inherits from the BaseModel
    """

    state_id = ""
    name = ""

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
