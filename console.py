#!/usr/bin/env python3

import cmd


class HBNBCommand(cmd.Cmd):
    prompt = '(hbnb) '

    def do_quit(self, args):
        """Quit command to exit the program
        """
        return True

    def do_EOF(self, args):
        """Quit command to exit the program
        """
        return True

    def emptyline(self):
        """called when an empty line is entered in response to the prompt"""
        pass


if __name__ == '__main__':
    HBNBCommand().cmdloop()
