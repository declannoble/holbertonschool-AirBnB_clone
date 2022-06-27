#!/usr/bin/python3
"""
Entry point for the AirBNB clone console
This contains and runs the CMD module and handles th entry point for the project
"""

import cmd

class HBNBCommand(cmd.Cmd):
    prompt = '(hbnb) '
    module_list = ["BaseModel"]

    def do_EOF(self, arg):
        """Exits console"""
        return True

    def emptyline(self):
        """ overwriting the emptyline method """
        return False

    def do_quit(self, arg):
        """Quit command to exit the program"""
        return True


if __name__ == '__main__':
    HBNBCommand().cmdloop()
