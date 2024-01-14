#!/usr/bin/python3
# My test module for testing my base model
"""Test base model module using unittesting"""

from models.base_model import BaseModel
from datetime import datetime
import unittest


class TestBaseModel(unittest.TestCase):
    """This is a unittest class for testing
    the base model module"""

    def test_init_wihtout_args(self):
        """Tests if the init works correctly"""
        obj = BaseModel()

        self.assertTrue(isinstance(obj.id, str))
        self.assertTrue(isinstance(obj.created_at, str))
        self.assertTrue(isinstance(obj.updated_at, str))

    def test_init_with_args(self):
        """Tests the init method with know arguments
        This is basically a resemblance of a dictionary"""
        obj_dict = {"id": "1324-MM-123",
                    "created_at": "2024-01-14T01:01:48.828338",
                    "updated_at": "2024-01-14T01:01:48.828338"}
        obj = BaseModel(**obj_dict)

        self.assertEqual(obj.id, obj_dict['id'])
        self.assertEqual(obj.created_at,
                         datetime.strptime(obj_dict['created_at'],
                                            '%Y-%m-%dT%H:%M:%S.%f'))
        self.assertEqual(obj.updated_at,
                         datetime.strptime(obj_dict['updated_at'],
                                            '%Y-%m-%dT%H:%M:%S.%f'))


if __name__ == "__main__":
    unittest.main()
