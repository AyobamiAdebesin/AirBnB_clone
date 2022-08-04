#!/usr/bin/python3
"""Defines the HBNBCommand class"""
import cmd
from models.base_model import BaseModel
from models.engine.file_storage import FileStorage
from models import storage


class HBNBCommand(cmd.Cmd):
    prompt = '(hbnb) '

    def do_quit(self, arg):
        'Quit command to exit the program'
        quit()
        return True

    def emptyline(self):
        pass

    def do_EOF(self):
        'EOF command'
        pass

    def do_create(self, arg):
        'Create command to create a new instance of BaseModel'
        if not arg:
            print("** class name missing **")
        elif arg != "BaseModel":
            print("** class doesn't exists**")
        elif arg == "BaseModel":
            new_model = BaseModel()
            storage.new(new_model)
            storage.save()
            print(new_model.id)

    def do_show(self, arg):
        '''
        Prints string representation of an
        instance based on class name and id
        '''
        split_args = arg.split()
        if len(split_args) == 0:
            print("** class name missing **")
        else:
            if split_args[0] != "BaseModel":
                print("** class doesn't exist **")
            elif split_args[0] == "BaseModel":
                try:
                    instance_key = f"{split_args[0]}.{split_args[1]}"
                    if instance_key in storage.all():
                        print(storage.all()[instance_key])
                except (IndexError):
                    print("** instance id missing **")
            else:
                print("** no instance found **")


if __name__ == "__main__":
    HBNBCommand().cmdloop()
