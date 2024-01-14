#!/usr/bin/python3
# review module
"""Review module"""


from models.place import Place


class Review(Place):
    """Review Class"""
    place_id = ''
    user_id = ''
    text = ''

    def __init__(self, *args, **kwargs):
        """init"""
        super().__init__(*args, **kwargs)
