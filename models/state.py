#!/usr/bin/python3
# state module
"""this is a class state that inherits base class"""


from models.base_model import BaseModel


class State(BaseModel):
    """class State which defines a state where
    an Airbnb place will be based"""
    name = ''

    def __init__(self, *args, **kwargs):
        """initializing method which inherits
        from the BaseModel init method"""
        super().__init__(*args, **kwargs)
