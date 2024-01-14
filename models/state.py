#!/usr/bin/python3
# state module
"""this is a class state that inherits base class"""


from base_model import BaseModel


class State(BaseModel):
    """class State"""

    def __init__(self):
        """initialization"""
        self.name = ''
