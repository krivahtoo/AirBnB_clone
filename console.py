#!/usr/bin/python3
# -*- encoding: utf-8 -*-
"""
    This is the console file
    Author: Peter Ekwere

"""
import cmd


class HBNBCommand(cmd.Cmd):
    """ This class manages the CMD methods """
    prompt = "(hbnb) "


    def do_EOF(self, args):
        return True



if __name__ == '__main__':
    HBNBCommand().cmdloop()
