#!/usr/bin/python3
'''
A class BaseModel
'''
import uuid
import datetime


class BaseModel:
    '''
    A class define the following public instances

    id: string - assign with an uuid
    created_at: assign with the current datetime when an instance is created
    updated_at: update the created_at
    '''

    # Public instance attributes initilization
    def __init__(self):
        ''' initialization of the calss attr '''
        # set the id with uuid 
        self.id = str(uuid.uuid4())
        # set created_at and updated_at with datetime
        self.created_at = datetime.datetime.now()
        self.updated_at = self.created_at

    # __str__ method
    def __str__(self):
        name = self.__name__
        _id = self.id
        _dict = self.__dict__

        return "[{}] ({}) {}".format(name, _id, _dict)
