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

    # set the promot
    prompt = "(hbnb) "

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
