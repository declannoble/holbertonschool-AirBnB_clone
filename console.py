#!/usr/bin/python3
"""
Entry point for the AirBNB clone console
This contains and runs the CMD module and handles th entry point for the project
"""

import cmd
import shlex
import models
from models.base_model import BaseModel

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
        if not self.verify_class_in_project(lineAsArgs):
            return
        newInstance = eval(str(lineAsArgs[0]) + '()')
        print(newInstance.id)
        newInstance.save()

    def do_show(self, arg):
        """Prints the string representation of an instance
based on the class name and id"""
        lineAsArgs = shlex.split(arg)
        if not self.verify_class_in_project(lineAsArgs):
            return
        if not self.verify_id_exists(lineAsArgs):
            return
        objectAsKey = str(lineAsArgs[0]) + '.' + str(lineAsArgs[1])
        objectsInStorage = models.storage.all()
        print(objectsInStorage[objectAsKey])

    def do_destroy(self, arg):
        """Deletes an instance based on the class name and id"""
        lineAsArgs = shlex.split(arg)
        if not self.verify_class_in_project(lineAsArgs):
            return
        if not self.verify_id_exists(lineAsArgs):
            return
        objectAsKey = str(lineAsArgs[0]) + '.' + str(lineAsArgs[1])
        models.storage.all().pop(objectAsKey)
        models.storage.save()

    def do_all(self, arg):
        """Prints list of strings of all instances or specified instances"""
        lineAsArgs = shlex.split(arg)
        objectsInStorage = models.storage.all()
        listOfObjectToPrint = []
        if len(lineAsArgs) == 0:
            for value in objectsInStorage.values():
                listOfObjectToPrint.append(str(value))
        else:
            if not self.verify_class_in_project(lineAsArgs):
                return
            for (key, value) in objectsInStorage.items():
                if lineAsArgs[0] in key:
                    listOfObjectToPrint.append(str(value))
        print(listOfObjectToPrint)

    def do_update(self, arg):
        """Deletes an instance based on the class name and id"""
        lineAsArgs = shlex.split(arg)
        if not self.verify_class_in_project(lineAsArgs):
            return
        if not self.verify_id_exists(lineAsArgs):
            return
        if not self.verify_attribute_arguments(lineAsArgs):
            return
        objectAsKey = str(lineAsArgs[0]) + '.' + str(lineAsArgs[1])
        setattr(models.storage.all()[objectAsKey], lineAsArgs[2], lineAsArgs[3])
        models.storage.all()[objectAsKey].save()

    @classmethod
    def verify_class_in_project(cls, args):
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
    def verify_id_exists(args):
        """verify that the ID being called exists"""
        if len(args) < 2:
            print("** instance id missing **")
            return False
        objects = models.storage.all()
        string_key = str(args[0]) + '.' + str(args[1])
        if string_key not in objects.keys():
            print("** no instance found **")
            return False
        return True

    @staticmethod
    def verify_attribute_arguments(args):
        """verify the attribute argument was passed correctly
        """
        if len(args) < 3:
            print("** attribute name missing **")
            return False
        if len(args) < 4:
            print("** value missing **")
            return False
        return True

if __name__ == '__main__':
    HBNBCommand().cmdloop()
