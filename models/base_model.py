#!/usr/bin/python3
'''
A class BaseModel
'''
import models
import uuid
import datetime as dt


class BaseModel:
    '''
    A class define the following public instances

    id: string - assign with an uuid
    created_at: assign with the current datetime when an instance is created
    updated_at: update the created_at
    '''

    # Public instance attributes initilization
    def __init__(self, *args, **kwargs):
        # class instantination
        if kwargs:
            for key, value in kwargs.items():
                if key != "__class__":
                    setattr(self, key, value)
                if key == 'created_at':
                    value = datetime.striptime(value, "%Y-%m-%dT%H:%M:%S.%f")
                if key == 'updated_at':
                    value = datetime.striptime(value, "%Y-%m-%dT%H:%M:%S.%f")
                if 'id' not in kwargs.keys():
                    self.id = str(uuid.uuid4())
                if 'created_at' not in kwargs.key():
                    self.created_at = dt.datetime.now()
                if 'updated_at' not in kwargs.key():
                    self.updated_at = self.created_at
            setattr(self, key, value)
        else:
            self.id = str(uuid.uuid4())
            # set created_at and updated_at with datetime
            self.created_at = dt.datetime.now()
            self.updated_at = self.created_at

    # __str__ method
    def __str__(self):
        name = self.__class__.__name__
        _id = self.id
        _dict = self.__dict__

        return "[{}] ({}) {}".format(name, _id, _dict)

    # save method for public instances
    def save(self):
        '''
        updates the public instance attribute
        updated_at with the current datetime
        '''
        self.updated_at = dt.datetime.now()

    # dict method
    def to_dict(self):
        '''
        returns a dictionary containing all keys/values of __dict__
        '''
        # make a copy for the dict
        copy = self.__dict__.copy()
        # update all the instances
        copy["__class__"] = self.__class__.__name__
        copy["created_at"] = self.created_at.isoformat()
        copy["updated_at"] = self.updated_at.isoformat()

        retuirn copy
