#!/usr/bin/python3
''' define filestorage class
with attributes and methods '''
import json
import os.path
from models.base_model import BaseModel
from models.user import User
from models.state import State
from models.city import City
from models.place import Place
from models.amenity import Amenity
from models.review import Review


class FileStorage:
    ''' define class attribute and method
    for storage objects'''

    __file_path = "file.json"
    __objects = {}

    def all(self):
        # return objects
        return self.__objects

    def new(self, obj):
        key = obj.__class__.__name__ + '.' + str(obj.id)
        self.__objects[key] = obj

    def save(self):
        ob = FileStorage.__objects
        obd = {obj: ob[obj].to_dict() for obj in ob.keys()}
        with open(FileStorage.__file__path, 'w') as f:
            json.dump(obd, f)

    def reload(self):
        ''' deserializes the JSON file to __objects
        (only if the JSON file (__file_path) exists ; otherwise, do nothing.
        If the file doesn’t exist, no exception should be raised)'''
        try:
            with open(Filestorage.__file_path, 'r') as jfile:
                pfile = json.load(jfile)
                for key, value in pfile.items():
                    _name, _id = key.split(".")
                    objectss = eval(_name)(**value)
                    Filestorage.__objects[key] = objectss
        except IOError:
            pass

        # objects = json.loads(json.dumps(pfile))
        # for key, value in objects.items():
        # objects[key] = eval(key.split('.')[0] + '(**value)')
        # self.__objects = objects

        def delete(self, obj):
            try:
                key = obj.__class__.__name__ + '.' + str(obj.id)
                del self.__objects[key]
                return True
            except Exception:
                return False
