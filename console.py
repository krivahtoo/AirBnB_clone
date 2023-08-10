#!/usr/bin/python3
# -*- encoding: utf-8 -*-
"""
    This is the console file
    Author: Peter Ekwere

"""
import cmd
from models.base_model import BaseModel
from models.engine.file_storage import FileStorage as storage


class HBNBCommand(cmd.Cmd):
    """ This class manages the CMD methods """
    prompt = "(hbnb) "

    class_names = {
            BaseModel : 'BaseModel'
            }

    def do_EOF(self, args):
        """ this function will implement the EOF command """
        return True

    def do_quit(self, args):
        """ Quit command to exit the program
        """
        return True

    def do_create(self, model):
        """ This function creates a New BaseModel instance """
        if model is None:
            print("** class name missing **")
        elif model not in self.class_names.values():
            print("** class doesn't exist **")
        else:
            for key, value in self.class_names.items():
                if model == value:
                    new_instance = key()
                    new_instance.save()
                    print(f"{new_instance.id}")

    def do_show(self, *args):
        """ The show function prints the base model id """
        if len(args) is None:
            print("** class name missing **")
        elif args[1] is None:
            print("** instance id missing")
        elif args[1] not in class_names.values():
            print("** class doesn't exist **")
        else:
            print(storage.all())




if __name__ == '__main__':
    HBNBCommand().cmdloop()
