#!/usr/bin/python3
""""""


import cmd
from models.base_model import BaseModel


class HBNBCommand(cmd.Cmd):
    """"""
    prompt = '(hbnb) '
    file = None

    def do_EOF(self, arg):
        """"""
        return True

    def help_EOF(self):
        """"""
        return True

    def do_quit(self, arg):
        """exiting the program"""
        exit()

    def help_quit(self):
        """"""
        print("Quit command to exit the program")
        return True

    def emptyline(self):
        """"""
        return False


if __name__ == '__main__':
    HBNBCommand().cmdloop()
