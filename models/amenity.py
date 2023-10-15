#!/usr/bin/env python3

from models.base_model import BaseModel


class Amenity:
    name = ""

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
