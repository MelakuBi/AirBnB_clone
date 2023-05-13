#!/usr/bin/ python3
'''
Console entry point of the command interpreter
'''
import cmd


class HBNBCommand(cmd.Cmd):
    '''
    Command interpreter command
    '''

    # set the promot
    prompt = '(hbnb)'

    def _quit(self, arg):
        ''' exit the program '''
        return True

    def _EOF(self, arg):
        ''' exit the program '''
        print()
        return True


if __name__ == '__main__':
    HBNBCommand().cmdloop()
