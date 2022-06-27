#!/usr/bin/python3
"""
Entry point for the AirBNB clone console
This contains and runs the CMD module and handles th entry point for the project
"""

import cmd
import shlex

class HBNBCommand(cmd.Cmd):
    prompt = '(hbnb) '
    listOfProjectClass = ["BaseModel"]

    def do_EOF(self, arg):
        """Exits console"""
        return True

    def emptyline(self):
        """ overwriting the emptyline method """
        return False

    def do_quit(self, arg):
        """Quit command to exit the program"""
        return True

    def do_create(self, arg):
        """Creates a new instance of a class and prints ID and saves to file"""
        lineAsArgs = shlex.split(arg)
        if not self.verify_class(lineAsArgs):
            return
        newInstance = eval(str(lineAsArgs[0]) + '()')
        print(newInstance.id)
        # need to code in the save to file aspect of this method when the
        # BaseModel is created

    def do_show(self, arg):
        """Prints the string representation of an instance
        based on the class name and id"""
        lineAsArgs = shlex.split(arg)
        if not self.verify_class(lineAsArgs):
            return
        if not self.verify_id(lineAsArgs):
            return
        # will have the code to display information here once we get a better idea of the project.

    @classmethod
    def verify_class(cls, args):
        """verify that class being created is defined in the project
        """
        if len(args) == 0:
            print("** class name missing **")
            return False
        if args[0] not in cls.listOfProjectClass:
            print("** class doesn't exist **")
            return False
        return True

    @staticmethod
    def verify_id(args):
        """verify that the ID being used exists"""
        #no idea how this will work just yet, will need to look at others code
        pass

if __name__ == '__main__':
    HBNBCommand().cmdloop()
