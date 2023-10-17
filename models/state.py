#!/usr/bin/python3
"""creates a sub class for Basemodel named, State
"""
from models.base_model import BaseModel


class State(BaseModel):
    """This file defines the State Model
    It inherits from the BaseModel
    """
    name = ""
