#!/usr/bin/python3
'''
Console entry point of the command interpreter
'''
import cmd


class HBNBCommand(cmd.Cmd):
    '''
    Command interpreter command
    '''

    # set the promot
    prompt = " (hbnb) "

    def do_quit(self, arg):
        ''' exit the program '''
        return True

    def do_EOF(self, arg):
        ''' exit the program '''
        print()
        return True


if __name__ == '__main__':
    HBNBCommand().cmdloop()
