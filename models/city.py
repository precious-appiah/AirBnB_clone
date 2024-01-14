#!/usr/bin/python3
# city module
"""this is a City module"""


from models.base_model import BaseModel


class City(BaseModel):
    """class City which inherits BaseModel"""
    def __init__(self):
        """initialization"""

        self.state_id = self.id
        self.name = ''
