#!/usr/bin/python3
# review module
"""Review module"""


from models.place import Place


class Review(Place):
    """Review Class which defines the base
    of a review"""
    place_id = ''
    user_id = ''
    text = ''

    def __init__(self, *args, **kwargs):
        """initializing method which inherits
        from the BaseModel init method"""
        super().__init__(*args, **kwargs)
