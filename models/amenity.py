#!/usr/bin/python3
# amenity module
"""amenity module"""

from models.base_model import BaseModel


class Amenity(BaseModel):
    """class Amenity which inherits
    from our BaseModel class"""
    name = ''

    def __init__(self, *args, **kwargs):
        """initializing method which inherits
        from the BaseModel init method"""
        super().__init__(*args, **kwargs)
