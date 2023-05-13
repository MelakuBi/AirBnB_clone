#!/usr/bin/python3
'''
Test cases for base_model.py using unittest
'''
import unittest
from models.base_model import BaseModel


class TestBaseModel(unittest.TestCase):
    '''
    Test class for base_model
    '''

    def init_test(self):
        '''
        function to test the __init__ function in base_model
        '''
        # check if the id is string
        _model = BaseModel()
        self.assertEqual(type(_model.id), str)



if __name__ == '__main__':
    unittest.main()
