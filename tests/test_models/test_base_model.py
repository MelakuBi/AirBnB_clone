#!/usr/bin/python3
'''
Test cases for base_model.py using unittest
'''
import unittest


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
        self.assertIsInstance(_model.id, str)
