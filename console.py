#!/usr/bin/python3
'''
Console entry point of the command interpreter
'''
from models.base_model import BaseModel
import cmd
import json
import shlex
from datetime import datetime


class HBNBCommand(cmd.Cmd):
    '''
    Command interpreter command
    '''

    # set the promot and classes
    prompt = "(hbnb) "
    classes = {"BaseModel"}

    # Create function to create a new instaces if not found
    def do_create(self, arg):
        ''' Creates a new instance of BaseModel'''
        if not arg:
            print("** class name missing **")

        # check if there is class name or not
        try:
            cls_name = models.class_for_name(arg)
        except NameError:
            print("** class doesn't exist **")
            return

        instance = cls()
        instance.save()
        print(instance.id)

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
