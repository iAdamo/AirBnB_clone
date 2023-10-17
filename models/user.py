#!/usr/bin/python3
"""
Module (user): This file defines the UserModel sub class
it inherits from BaseModel

"""

from models.base_model import BaseModel


class User(BaseModel):
    """User models

    Args:
        email: string - empty string
        password: string - empty string
        first_name: string - empty string
        last_name: string - empty string
    """
    email = ""
    password = ""
    first_name = ""
    last_name = ""
