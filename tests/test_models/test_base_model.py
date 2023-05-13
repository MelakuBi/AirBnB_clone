#!/usr/bin/python3
'''
Test cases for base_model.py using unittest
'''
import unittest
from models.base_model import BaseModel
from datetime import datetime

class TestBaseModel(unittest.TestCase):
    '''
    Test class for base_model
    '''

    def setUp(self):
        self._model = BaseModel()

    def test_init(self):
        '''
        function to test the __init__ function in base_model
        '''
        # check if the id is string
        _model = BaseModel()
        self.assertEqual(str, type(_model.id))

        # check the typt of datetime
        self.assertEqual(datetime, type(_model.created_at))
        self.assertEqual(datetime, type(_model.updated_at))

        # check __str__ method
        _id = _model.id
        _dict = _model.__dict__
        output = "[BaseModel] ({}) {}".format(_id, _dict)
        self.assertEqual(str(_model), output)

    def test_save(self):
        '''
        Function to test the save function inside BaseModel
        '''

        old = BaseModel().updated_at
        BaseModel().save()
        self.assertNotEqual(BaseModel().save(), old)

    def test_to_dict(self):
        '''
        Function to test the to_dict function inside BaseModel
        '''

        my_model = self._model
        my_dict = self._model.to_dict()
        self.assertIsInstance(my_dict, dict)
        self.assertIn("__class__", my_dict)
        self.assertIn("id", my_dict)
        self.assertIn("created_at", my_dict)
        self.assertIn("updated_at", my_dict)

        # check th values of all instances

        self.assertEqual(my_model.__class__.__name__, my_dict["__class__"])
        self.assertEqual(my_model.id, my_dict["id"])
        
        iso_created = my_model.created_at.isoformat()
        self.assertEqual(iso_created, my_dict["created_at"])

        iso_updated = my_model.updated_at.isoformat()
        self.assertEqual(iso_updated, my_dict["created_at"])


if __name__ == '__main__':
    unittest.main()
