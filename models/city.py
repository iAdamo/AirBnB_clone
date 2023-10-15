#!/usr/bin/env python3
"""
creates a sub class for Basemodel named, City
"""
from .base_model import BaseModel


class City(BaseModel):
    state_id = ""
    name = ""

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
