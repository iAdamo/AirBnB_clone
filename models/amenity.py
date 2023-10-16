#!/usr/bin/python3
"""
creates a sub class for Basemodel named, Amenity
"""

from models.base_model import BaseModel


class Amenity(BaseModel):
    """
    A subclass to inherit from Basemodel.

    Amenity module is inheriting gtom the main class.
    """

    name = ""

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
