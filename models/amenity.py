#!/usr/bin/python3
"""
creates a sub class for Basemodel named, Amenity
"""

from models.base_model import BaseModel


class Amenity(BaseModel):
    """Amenity module is inheriting from the main class.
    """
    name = ""
