#!/usr/bin/python3
# -*- encoding: utf-8 -*-
"""
    This is the console file
    Author: Peter Ekwere

"""
import cmd
from models.base_model import BaseModel
from models.user import User
from models.state import State
from models.review import Review
from models.city import City
from models.place import Place
from models.amenity import Amenity
from models.__init__ import storage
from models.engine.file_storage import FileStorage


class HBNBCommand(cmd.Cmd):
    """ This class manages the CMD methods """
    prompt = "(hbnb) "

    class_names = {
            BaseModel: 'BaseModel',
            User: 'User',
            Amenity: 'Amenity',
            City: 'City',
            Place: 'Place',
            Review: 'Review',
            State: 'State'
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

    def do_show(self, args):
        """ The show function prints the base model id """
        argument = args.split()

        if len(argument) == 0:
            print("** class name missing **")
        elif len(argument) == 1:
            print("** instance id missing")
        elif argument[0] not in self.class_names.values():
            print("** class doesn't exist **")
        else:
            for key, value in self.class_names.items():
                if argument[0] == value:
                    class_dict = storage.all()
                    instance = f"{argument[0]}.{argument[1]}"
                    if instance not in class_dict:
                        print("** no instance found **")
                    else:
                        instance_dict = class_dict[instance]
                        print(instance_dict)
                        storage.save()

    def do_destroy(self, args):
        """ The destroy function Deletes an instance """
        argument = args.split()

        if len(argument) == 0:
            print("** class name missing **")
        elif len(argument) == 1:
            print("** instance id missing")
        elif argument[0] not in self.class_names.values():
            print("** class doesn't exist **")
        else:
            instance = f"{argument[0]}.{argument[1]}"
            class_dict = storage.all()
            if instance not in class_dict:
                print("** no instance found **")
            else:
                del class_dict[instance]
                storage.save()

    def do_all(self, model):
        """ The all function prints a list of all the instances """
        if len(model) > 0 and model not in self.class_names.values():
            print("** class doesn't exist **")
        else:
            class_dict = storage.all()
            object_list = []

            for a_object in class_dict:
                if len(model) > 0 and model == a_object.__class__:
                    object_list.append(str(class_dict[a_object]))
                else:
                    object_list.append(str(class_dict[a_object]))
            print(object_list)

    def do_update(self, model):
        """ The update function updates the attribute of an instance """
        class_dict = storage.all()
        argument = model.split()

        if len(argument) == 0:
            print("** class name missing **")
        elif len(argument) == 1:
            print("** instance id missing")
        elif len(argument) == 2:
            print("** attribute name missing **")
        elif len(argument) == 3:
            print("** value missing **")
        elif argument[0] not in self.class_names.values():
            print("** class doesn't exist **")
        else:
            instance_id = f"{argument[0]}.{argument[1]}"
            attribute = argument[2]
            value = argument[3]
            a_obj = class_dict[instance_id]
            if instance_id not in class_dict:
                print("** no instance found **")
            else:
                if attribute in a_obj.__class__.__dict__.keys():
                    attribute_type = type(a_obj.__class__.__dict__[attribute])
                    a_obj.__dict__[attribute] = attribute_type(value)
                else:
                    a_obj.__dict__[attribute] = value
            storage.save()


if __name__ == '__main__':
    HBNBCommand().cmdloop()
