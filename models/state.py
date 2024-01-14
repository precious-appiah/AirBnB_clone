#!/usr/bin/python3
# state module
"""this is a class state that inherits base class"""


from models.base_model import BaseModel


class State(BaseModel):
    """class State"""
    name = ''

    def __init__(self, *args, **kwargs):
        """init"""
        super().__init__(*args, **kwargs)
