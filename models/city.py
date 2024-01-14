#!/usr/bin/python3
# city module
"""this is a City module"""


from models.base_model import BaseModel


class City(BaseModel):
    """class City which inherits BaseModel"""
    state_id = ''
    name = ''

    def __init__(self, *args, **kwargs):
        """init"""
        super().__init__(*args, **kwargs)
