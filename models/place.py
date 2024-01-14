#!/usr/bin/python3
# place module
"""place module"""

from .city import City


class Place(City):
    """class Place"""
    city_id = ''
    user_id = ''
    name = ''
    description = ''
    number_rooms = 0
    number_bathrooms = 0
    max_guest = 0
    price_by_night = 0
    latitude = 0.0
    longitude = 0.0
    amenity_ids = ['']

    def __init__(self):
        """init"""
        self.city_id = self.city_id
        self.user_id = '' """to be updated"""
        self.name = ''
        self.description = ''
        self.number_rooms = 0
        self.number_bathrooms = 0
        self.max_guest = 0
        self.price_by_night = 0
        self.latitude = 0.0
        self.longitude = 0.0
        self.amenity_ids = ['']
