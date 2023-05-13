#!/usr/bin/python3
''' define filestorage class
with attributes and methods '''
import json
from models.base_model import basemodel
from models.user import User
from models.state import State
from models.city import City
from models.place import Place
from models.amenity import Amenity
from models.review import Review


class Filestorage:
    ''' define class attribute and method
    for storage objects'''

    __file_path = "file.json"
    _objects = {}

    def all(self):
        # return objects
        return self._objects

    def new(self, obj):
        key = obj.__class__.__name__ + '.' + obj.id
        __objectcts[key] = obj

    def save(self):
        converted = {}
        for key, value in self.__objects.items():
            converted[key] = value.to_dict()
            with open(self.__file_path, w) as jfile:
                jfile = json.dumps(converted)

    def reload(self):
        ''' deserializes the JSON file to __objects
        (only if the JSON file (__file_path) exists ; otherwise, do nothing.
        If the file doesn’t exist, no exception should be raised)'''
        try:
            with open(self.__file_path, 'r') as jfile:
                pfile = json.load(jfile)
        except Exception:
            return
        objects = eval(pfile)
        for key, val in objects.items():
            objects[key] = eval(key.split('.')[0] + '(**value)')
            self.__objects = objects

        def delete(self, obj):
            try:
                key = obj.__class__.__name__ + '.' + str(obj.id)
                del self.__objects[key]
                return True
            except Exception:
                return False
