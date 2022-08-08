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
    prompt = '(hbnb) '
    class_dict = {
            "BaseModel": BaseModel, "User": User,
            "Amenity": Amenity, "Place": Place,
            "City": City, "State": State, "Review": Review}
    
    class_list = ["BaseModel",
               "User",
               "Place",
               "State",
               "City",
               "Amenity",
               "Review"]

    def do_quit(self, arg):
        '''
        Quit command to exit the program
        Type "quit" to exit
        '''
        return True

    def emptyline(self):
        pass

    def do_EOF(self, arg):
        '''
        EOF command to exit the program
        Press "Ctrl + D"
        '''
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
            print("** class doesn't exist **")
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
            print("** class doesn't exist **")

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
            print("** class name missing **")
    
    def default(self, line: str) -> None:
        commands = ["show",
                    "all()",
                    "destroy",
                    "update",
                    "count()"]
        line = line.split('.')
        try:
            if line[0] in self.classes:
                if line[1] == commands[1]:
                    self.do_all(line[0])
                elif line[1] == commands[4]:
                    res = []
                    for key in storage.all():
                        if key.split('.')[0] == line[0]:
                            res.append(str(storage.all()[key]))
                    print(len(res))
                elif line[1].split('(')[0] == commands[0]:
                    key = line[0] + "." + line[1].split('(')[1][1:-2]
                    if key in storage.all():
                        print(storage.all()[key])
                    else:
                        print('** no instance found **')
                elif line[1].split("(")[0] == commands[2]:
                    key = line[0] + "." + line[1].split('(')[1][1:-2]
                    if key in storage.all():
                        storage.all().__delitem__(key)
                        storage.save()
                    else:
                        print('** no instance found **')
                elif line[1].split("(")[0] == commands[3]:
                    if line[1][-2] != "}":
                        data = line[1].split("(")[1][1:-2].split('", "')
                        key = line[0] + "." + data[0]
                        if key in storage.all() and len(data[2].split()) != 0:
                            try:
                                if data[1] in storage.all()[key].to_dict():
                                    try:
                                        setattr(storage.all()[key],
                                                data[1], data[2])
                                        storage.all()[key].save()
                                    except (IndexError):
                                        print("** value missing **")
                                else:
                                    try:
                                        setattr(storage.all()[key],
                                                data[1], data[2])
                                        storage.all()[key].save()
                                    except (IndexError):
                                        print("** value missing **")
                            except (IndexError):
                                print("** attribute name missing **")
                        else:
                            print('** no instance found **')
                    else:
                        data = line[1].split("(")[1][1:-1].split('", ')
                        key = line[0] + "." + data[0]
                        new_dict = '", '.join(data[1:])
                        if key in storage.all():
                            try:
                                new_dict = literal_eval(new_dict)
                                if len(new_dict) == 0:
                                    print("** attribute name missing **")
                                elif type(new_dict) == set:
                                    print("** value missing **")
                                else:
                                    for k in new_dict:
                                        setattr(storage.all()[key], k,
                                                new_dict[k])
                                        storage.all()[key].save()
                            except (IndexError, SyntaxError):
                                print("omoo this your dictionary ehn")
                        else:
                            print('** no instance found **')
                else:
                    print("** command not found **")
            else:
                print("*** Unknown syntax:", line[0])
        except (IndexError):
            print("*** Unknown syntax:", line)


if __name__ == "__main__":
    HBNBCommand().cmdloop()
