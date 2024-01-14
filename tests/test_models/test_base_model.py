#!/usr/bin/python3
# My test module for testing my base model
"""Test base model module using unittesting"""

from models.base_model import BaseModel
import unittest


class TestBaseModel(unittest.TestCase):
    """This is a unittest class for testing
    the base model module"""

    def test_init(self):
        """Tests if the init works correctly"""
        obj = BaseModel()

        self.assertTrue(isinstance(obj.id, str))

if __name__ == "__main__":
    unittest.main()
