#!/usr/bin/python3
"""User definition module"""
from models.base_model import BaseModel


class User(BaseModel):
    """Class that defines a User for the
    AirBnB clone project"""

    email = ''
    password = ''
    first_name = ''
    last_name = ''

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
