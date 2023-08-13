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

    def do_emptyline(self, args):
        """ This function will implemetn the emptyline """
        return False

    def do_help(self, args):
        """ overide help method """
        cmd.Cmd.do_help(self, args)

    def precmd(self, args):
        """ This will ovewrite default precmd """
        if "." in args:
            args = args.replace(".", " ").replace("(", " ").replace(")", " ")
            args = args.split(" ")
            if len(args) >= 3:
                command = args[1]
                Class = args[0]
                ID = args[2]
                args = f"{command} {Class} {ID}"
            elif len(args) == 2:
                command = args[1]
                Class = args[0]
                args = f"{command} {Class}"
            elif len(args) >= 4:
                command = args[1]
                Class = arg[0]
                ID = args[2]
                args = f"{command} {Class} {ID} {args[3]} {args[4]}"

        return cmd.Cmd.precmd(self, args)

    def do_create(self, model):
        """ This function creates a New BaseModel instance """
        if model is None or len(model) < 1:
            print("** class name missing **")
            return False
        elif model not in self.class_names.values():
            print("** class doesn't exist **")
            return False
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
            return False
        elif len(argument) == 1:
            print("** instance id missing **")
            return False
        elif argument[0] not in self.class_names.values():
            print("** class doesn't exist **")
            return False
        else:
            for key, value in self.class_names.items():
                if argument[0] == value:
                    class_dict = storage.all()
                    instance = f"{argument[0]}.{argument[1]}"
                    if instance not in class_dict:
                        print("** no instance found **")
                        return False
                    else:
                        instance_dict = class_dict[instance]
                        print(instance_dict)
                        storage.save()

    def do_destroy(self, args):
        """ The destroy function Deletes an instance """
        argument = args.split()

        if len(argument) == 0:
            print("** class name missing **")
            return False
        elif len(argument) == 1:
            print("** instance id missing")
            return False
        elif argument[0] not in self.class_names.values():
            print("** class doesn't exist **")
            return False
        else:
            instance = f"{argument[0]}.{argument[1]}"
            class_dict = storage.all()
            if instance not in class_dict:
                print("** no instance found **")
                return False
            else:
                del class_dict[instance]
                storage.save()

    def do_all(self, args):
        """ The all function prints a list of all the instances """
        model = args.split()
        if len(model) > 1:
            return False
        elif len(model) == 1:
            Class = model[0]
            class_dict = storage.all()
            object_list = []

            if Class not in self.class_names.values():
                print("** class doesn't exist")
                return False

            for key, value in class_dict.items():
                class_name = value.__class__.__name__
                if Class == class_name:
                    object_list.append(str(class_dict[key]))
            print(object_list)
        else:
            class_dict = storage.all()
            object_list = []

            for a_object in class_dict:
                object_list.append(str(class_dict[a_object]))
            print(object_list)

    def do_count(self, model):
        """ This Function will count and return number of instances """
        class_dict = storage.all()
        argument = model.split()

        if len(argument) == 0:
            print("** class name missing **")
        elif len(argument) > 0:
            Class = argument[0]
            count = 0

            if Class not in self.class_names.values():
                print("** class doesn't exist")
                return False
            else:
                for key, value in class_dict.items():
                    class_name = value.__class__.__name__
                    if Class == class_name:
                        count += 1
                print(count)

    def do_update(self, model):
        """ The update function updates the attribute of an instance """
        class_dict = storage.all()
        argument = model.split()

        if len(argument) == 0:
            print("** class name missing **")
            return False
        elif len(argument) == 1:
            print("** instance id missing")
            return False
        elif len(argument) == 2:
            print("** attribute name missing **")
            return False
        elif len(argument) == 3:
            print("** value missing **")
            return False
        elif argument[0] not in self.class_names.values():
            print("** class doesn't exist **")
            return False
        else:
            instance_id = f"{argument[0]}.{argument[1]}"
            attribute = argument[2]
            value = argument[3]
            a_obj = class_dict[instance_id]
            if instance_id not in class_dict:
                print("** no instance found **")
                return False
            else:
                if attribute in a_obj.__class__.__dict__.keys():
                    attribute_type = type(a_obj.__class__.__dict__[attribute])
                    a_obj.__dict__[attribute] = attribute_type(value)
                else:
                    a_obj.__dict__[attribute] = value
            storage.save()


if __name__ == '__main__':
    HBNBCommand().cmdloop()
