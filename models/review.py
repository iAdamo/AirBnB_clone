#!/usr/bin/python3
"""creates a sub class for Basemodel named, Review
"""
from models.base_model import BaseModel


class Review(BaseModel):
    """This file defines the Review Model
    It inherits from the BaseModel
    """
    place_id = ""
    user_id = ""
    text = ""
