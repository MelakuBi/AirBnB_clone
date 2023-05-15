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

    # All functon to print string representation of all instances
    def do_all(self, arg):
        '''
        Prints all string representation of all
        instances based or not on the class name
        '''
        if not arg:
            print("** class name missing **")
        elif arg not in self.classes:
            print("** class doesn't exist **")
        else:
            objects = models.storage.all()
            print(objects)

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
    
    # Update function to update instance based on
    # the class name and id by adding or updating attribute
    def do_update(self, arg):
        '''
        Updates an instance based on
        the class name and id by adding or updating attribute
        '''
        arg_parts = arg.split()
        if not arg or arg_parts == 0:
            print("** class name missing **")
            return
        
        if len(arg_parts) < 2:
            print("** instance id missing **")
            return
        
        _name, _id = arg_parts[0], arg_parts[1]
        if _name not in self.classes:
            print("** class doesn't exist **")
            return
        if len(arg_parts) < 3:
            print("** attribute name missing **")
            return
        if len(arg_parts) < 4:
            print("** value missing **")
            return

        attr_name, attr_value = args[2], args[3]
        objects = models.storage.all()
        key = class_name + "." + obj_id
        obj = objects.get(key)

        if obj is None:
            print("** no instance found **")
            return

        try:
            setattr(obj, attr_name, eval(attr_value))
        except AttributeError:
            print("** no instance found **")
            return
        models.storage.save()

    # Destroy function to deletes an instance
    def do_destroy(self, arg):
        '''
        Deletes an instance based on the class name and id
        '''
        if not arg:
            print("** class name missing **")
        else:
            objects = models.storage.all()
            try:
                _name, _id = arg.split()
                key = _name + "." + _id
                del(objects[key])
                models.storage.save()
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
