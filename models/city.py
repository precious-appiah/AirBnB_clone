#!/usr/bin/python3
# city module
"""this is a City module"""


from models.base_model import BaseModel


class City(BaseModel):
    """class City which inherits BaseModel
    class and defines a city"""
    state_id = ''
    name = ''

    def __init__(self, *args, **kwargs):
        """initializing method which inherits
        from the BaseModel init method"""
        super().__init__(*args, **kwargs)
