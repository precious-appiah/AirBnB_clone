#!/usr/bin/python3
# amenity module
"""amenity module"""

from base_model import BaseModel


class Amenity(BaseModel):
    """class Amenity"""
    name = ''

    def __init__(self):
        self.name = ''
