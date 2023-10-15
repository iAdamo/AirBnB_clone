#!/usr/bin/env python3
"""
creates a sub class for Basemodel named, State
"""
from models.base_model import BaseModel


class State(BaseModel):
    name = ""

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
