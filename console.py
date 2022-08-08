#!/usr/bin/python3
"""Defines the HBNBCommand class"""
import cmd

from models.base_model import BaseModel
from models.user import User
from models.state import State
from models.city import City
from models.review import Review
from models.amenity import Amenity
from models.place import Place
from models.engine.file_storage import FileStorage
from models import storage


class HBNBCommand(cmd.Cmd):
    intro = 'Welcome to HBNB Console      Type "help" or ? to list commands.\n'
    prompt = '(hbnb) '
    class_dict = {
            "BaseModel": BaseModel, "User": User,
            "Amenity": Amenity, "Place": Place,
            "City": City, "State": State, "Review": Review}

    def do_quit(self, arg):
        '''
        Quit command to exit the program
        Type "quit" to exit
        '''
        quit()
        return True

    def emptyline(self):
        pass

    def do_EOF(self, arg):
        '''
        EOF command to exit the program
        Press "Ctrl + D"
        '''
        quit()
        return True

    def do_create(self, arg):
        '''
        Create command to create a new instance of BaseModel\n
        Usage: create <class name>
        Ex: create BaseModel
        '''
        if not arg:
            print("** class name missing **")
        elif arg not in HBNBCommand.class_dict:
            print("** class doesn't exists**")
        else:
            new_model = HBNBCommand.class_dict[arg]()
            storage.new(new_model)
            storage.save()
            print(new_model.id)

    def do_show(self, arg):
        '''
        Prints string representation of an
        instance based on class name and id\n
        Usage: show <class name> <object id>
        Ex: show BaseModel 1234-1234-1234
        '''
        split_args = arg.split()
        if len(split_args) == 0:
            print("** class name missing **")
        else:
            if split_args[0] not in HBNBCommand.class_dict:
                print("** class doesn't exist **")
            elif split_args[0] in HBNBCommand.class_dict:
                try:
                    instance_key = f"{split_args[0]}.{split_args[1]}"
                    if instance_key in storage.all():
                        print(storage.all()[instance_key])
                    else:
                        print("** no instance found **")
                except (IndexError):
                    print("** instance id missing **")

    def do_destroy(self, arg):
        '''
        Deletes an instance based on class name and id\n
        Usage: delete <class name> <class id>
        Ex: delete BaseModel 1234-1234-1234
        '''
        split_args = arg.split()
        if len(split_args) == 0:
            print("** class name missing **")
        else:
            if split_args[0] not in HBNBCommand.class_dict:
                print("** class doesn't exist **")
            elif split_args[0] in HBNBCommand.class_dict:
                try:
                    instance_key = f"{split_args[0]}.{split_args[1]}"
                    if instance_key in storage.all():
                        del storage.all()[instance_key]
                        storage.save()
                    else:
                        print("** no instance found **")
                except (IndexError):
                    print("** instance id missing **")

    def do_all(self, arg):
        '''
        Prints all string representation of all instances\n
        Usage: all / all <class name>
        ex: $ all BaseModel / all
        '''
        if not arg:
            instance_list = []
            for key, value in storage.all().items():
                instance_list.append(str(value))
            print(instance_list)
        elif arg in HBNBCommand.class_dict:
            class_name = HBNBCommand.class_dict[arg]
            instance_list_arg = []
            for key, value in storage.all().items():
                if getattr(value, '__class__') == class_name:
                    instance_list_arg.append(str(value))
            print(instance_list_arg)
        elif arg not in HBNBCommand.class_dict:
            print("** class doesn't exist**")

    def do_update(self, arg):
        '''
        Updates an instance based on the class name and id\n
        Usage: $ update <class name> <id> <attribute name> "<attribute value>"
        '''
        split_args = arg.split()

        try:
            if split_args[0] not in HBNBCommand.class_dict:
                print("** class doesn't exist **")
            else:
                try:
                    instance_key = f"{split_args[0]}.{split_args[1]}"
                    if instance_key in storage.all():
                        get_obj = storage.all()[instance_key]
                        try:
                            attr_name = split_args[2]
                            try:
                                attr_value = split_args[3]
                                setattr(get_obj, attr_name, attr_value)
                                storage.save()
                            except (IndexError):
                                print("** value missing **")
                        except (IndexError):
                            print("** attribute name missing **")
                    else:
                        print("** no instance found **")
                except (IndexError):
                    print("** instance id missing **")
        except (IndexError):
            print("** class name is missing **")


if __name__ == "__main__":
    HBNBCommand().cmdloop()
