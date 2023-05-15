#!/usr/bin/python3
'''
Console entry point of the command interpreter
'''
from models.base_model import BaseModel
import cmd
import json
import shlex
from datetime import datetime
import models


class HBNBCommand(cmd.Cmd):
    '''
    Command interpreter command
    '''

    # set the promot and classes
    prompt = "(hbnb) "
    classes = [
            "BaseModel", "User", "State", "City", "Amenity", "Place", "Review"
            ]

    # Create function to create a new instaces if not found
    def do_create(self, arg):
        ''' Creates a new instance of BaseModel'''
        _name = arg
        if not arg:
            print("** class name missing **")

        # check if there is class name or iD
        elif _name not in self.classes:
            print("** class doesn't exist **")

        try:
            cls = globals()[arg]
        except Exception:
            return
        instance = cls()
        print(instance.id)

    # show function to Prints the string representation of an instance
    def do_show(self, arg):
        '''
        Prints the string representation of an instance
        based on the class name and id
        '''
        if not arg:
            print("** class name missing **")
        else:
            objects = models.storage.all()
            try:
                _name, _id = arg.split()
                key = _name + "." + _id
                print(objects[key])
            except ValueError:
                if arg in self.classes:
                    print("** instance id missing **")
                else:
                    print("** class doesn't exist **")
            except KeyError:
                print("** no instance found **")

    # quit function to exit the program
    def do_quit(self, arg):
        ''' exit the program '''
        return True

    def do_EOF(self, arg):
        ''' exit the program '''
        print()
        return True

    def emptyline(self):
        pass


if __name__ == '__main__':
    HBNBCommand().cmdloop()
