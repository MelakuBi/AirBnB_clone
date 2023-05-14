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
    classes = {"BaseModel"}

    # Create function to create a new instaces if not found
    def do_create(self, arg):
        ''' Creates a new instance of BaseModel'''
        if not arg:
            print("** class name missing **")

        # check if there is class name or iD
        elif arg not in self.classes:
            print("** class doesn't exist **")

    # show function to Prints the string representation of an instance
    def do_show(self, arg):
        '''
        Prints the string representation of an instance
        based on the class name and id
        '''
        if not arg:
            print("** class name missing **")
            return
        # find the number of arguments inserted
        arg = arg.split()

        # check the length of the arguments
        if len(arg) < 2:
            print("** instance id missing **")
            return

        # check the name of the class and the id presence
        
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
