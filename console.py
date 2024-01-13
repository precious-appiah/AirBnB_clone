#!/usr/bin/env python3
"""this is a console program"""


import cmd
from models.base_model import BaseModel
from models import storage


class HBNBCommand(cmd.Cmd):
    """class for hbnb command line"""
    """quit and EOF"""
    """help, prompt, """
    class_names = ['BaseModel']
    prompt = '(hbnb)'

    def do_quit(self, line):
        """function to quit the program"""
        return True

    def do_EOF(self, line):
        """function to quit the program"""
        return True

    def emptyline(self):
        """handle empty line"""
        pass

    def do_create(self, line):
        """function to create an instance """
        if len(line) == 0:
            print('** class name missing **')
        elif line not in self.class_names:
            print("** class doesn't exist **")
        else:
            new_model = globals()[line]()
            new_model.save()
            print("{}".format(new_model.id))

    def do_show(self, line):
        """to print the string repressentation"""
        line_arr = line.split(' ')
        if len(line) == 0:
            print('** class name missing **')
        elif line_arr[0] not in self.class_names:
            print("** class doesn't exist **")
        elif len(line_arr) != 2:
            print('** instance id missing **')
        else:
            name = line_arr[0] + '.' + line_arr[1]
            my_new_model = BaseModel(**storage.reload()[name])
            print(type(my_new_model))


if __name__ == '__main__':
    HBNBCommand().cmdloop()
