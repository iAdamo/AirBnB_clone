#!/usr/bin/env python3

import cmd
from models.base_model import BaseModel
from models import storage
from models.user import User
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.place import Place
from models.review import Review


class HBNBCommand(cmd.Cmd):
    """entry point of the command interpreter
    """

    intro = "A command interpreter to manipulate AirBnB data"
    prompt = '(hbnb) '

    objects = [
            'BaseModel', 'User', 'State', 'City',
            'Amenity', 'Place', 'Review'
            ]

    def do_quit(self, args):
        """Quit command to exit the program
        """
        return True

    def do_EOF(self, args):
        """Quit command to exit the program
        """
        return True

    def postloop(self):
        """Hook method executed once when cmdloop() is about to return
        """
        print()

    def emptyline(self):
        """called when an empty line is entered in response to the prompt"""
        pass

    def do_create(self, args):
        """Creates a new instance of BaseModel, saves it (to the JSON file)
        and prints the id. Ex: $ create BaseModel

        Return:
            The id of the instance
        """
        if args == '':
            print("** class name missing **")
        elif args in HBNBCommand.objects:
            my_model = eval(args + '()')
            my_model.save()
            print(my_model.id)
        else:
            print("** class doesn't exist **")

    def do_show(self, args):
        """Prints the string representation of an instance based on the
        class name and id. Ex: $ show BaseModel 1234-1234-1234

        Return:
            The string representation of the object id
        """
        args_list = args.split()
        if args == "":
            print("** class name missing **")
        elif args_list[0] in HBNBCommand.objects:
            if len(args_list) < 2:
                print("** instance id missing **")
                return False
            all_objs = storage.all()
            obj_id = f"{args_list[0]}.{args_list[1]}"
            if obj_id not in all_objs.keys():
                print("** no instance found **")
            else:
                print(all_objs[obj_id])
        else:
            print("** class doesn't exist **")

    def do_destroy(self, args):
        """ Deletes an instance based on the class name and id (save the change
        into the JSON file). Ex: $ destroy BaseModel 1234-1234-1234

        Return:
            Nothing
        """
        args_list = args.split()
        if args == "":
            print("** class name missing **")
        elif args_list[0] in HBNBCommand.objects:
            if len(args_list) < 2:
                print("** instance id missing **")
                return False
            all_objs = storage.all()
            obj_id = f"{args_list[0]}.{args_list[1]}"
            if obj_id not in all_objs.keys():
                print("** no instance found **")
            else:
                del all_objs[obj_id]
                storage.save()
        else:
            print("** class doesn't exist **")

    def do_all(self, args):
        """Prints all string representation of all instances based or not
        on the class name. Ex: $ all BaseModel or $ all.

        Return:
            (list) The printed result must be a list of strings
        """
        args_list = args.split()
        if args == "":
            str_rep = []
            all_objs = storage.all()
            for obj_id in all_objs.keys():
                str_rep.append(str(all_objs[obj_id]))
            print(str_rep)
        elif args_list[0] in HBNBCommand.objects:
            str_rep = []
            all_objs = storage.all()
            for obj_id, value in all_objs.items():
                if obj_id[:-37] == args_list[0]:
                    str_rep.append(str(all_objs[obj_id]))
            print(str_rep)
        else:
            print("** class doesn't exist **")

    def do_update(self, args):
        """Updates an instance based on the class name and id by adding or
        updating attribute (save the change into the JSON file).
        Ex: $ update BaseModel 1234-1234-1234 email "aibnb@mail.com"
        """
        args_list = args.split()
        if args == "":
            print("** class name missing **")
        elif args_list[0] in HBNBCommand.objects:
            if len(args_list) < 2:
                print("** instance id missing **")
                return False
            all_objs = storage.all()
            obj_id = f"{args_list[0]}.{args_list[1]}"
            if obj_id not in all_objs.keys():
                print("** no instance found **")
            else:
                if len(args_list) < 3:
                    print("** attribute name missing **")
                    return False
                elif len(args_list) < 4:
                    print("** value missing **")
                    return False
                if args_list[3].startswith('"') and args_list[3].endswith('"'):
                    args_list[3] = args_list[3][1:-1]
                key = f"{args_list[0]}.{args_list[1]}"
                setattr(all_objs[key], args_list[2], args_list[3])
                storage.save()
        else:
            print("** class doesn't exist **")


if __name__ == '__main__':
    HBNBCommand().cmdloop()
