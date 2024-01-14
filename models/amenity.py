#!/usr/bin/python3
# amenity module
"""amenity module"""

from models.base_model import BaseModel


class Amenity(BaseModel):
    """class Amenity"""
    name = ''

    def __init__(self, *args, **kwargs):
        """init"""
        super().__init__(*args, **kwargs)
