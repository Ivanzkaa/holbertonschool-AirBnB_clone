#!/usr/bin/python3
"""Before the module and the class"""


import cmd
from models.base_model import BaseModel


class HBNBCommand(cmd.Cmd):
    """the hbnb class"""
    prompt = '(hbnb) '
    file = None

    def do_EOF(self, arg):
        """the end of file"""
        return True

    def help_EOF(self):
        """command of help end of file"""
        return True

    def do_quit(self, arg):
        """exiting the program"""
        exit()

    def help_quit(self):
        """help quitting"""
        print("Quit command to exit the program")
        return True

    def emptyline(self):
        """the empty line"""
        return False


if __name__ == '__main__':
    HBNBCommand().cmdloop()
