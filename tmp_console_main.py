#!/usr/bin/python3
"""called console that contains the entry point of the command interpreter
"""
import cmd
import os
from models.all_models import our_models
from models import storage


class HBNBCommand(cmd.Cmd):
    """ simple command processor Example"""

    prompt = '(hbnb) '

    def do_shell(self, line):
        """excute shell commands
        Usage: shell<command> or !<command>
        """
        output = os.popen(line).read()
        print(output)

    def do_EOF(self, line):
        """EOF command to exit the program
        Usage: EOF
        """
        return True

    def emptyline(self):
        """overrides for original func"""
        pass

    def do_quit(self, line):
        """Quit command to exit the program
        Usage: quit
        """
        return True

    def do_create(self, line):
        """creates new instace as save it to json file
        Usage: create <className>
        """
        args = line.split()
        if not line:
            print("** class name missing **")
        elif args[0] not in our_models.keys():
            print("** class doesn't exist **")
        else:
            storage.reload()
            self.my_model = our_models[args[0]]()
            print(self.my_model.id)
            for i in range(1, len(args)):
                key, value = args[i].split("=")
                try:
                    value = int(value)
                except ValueError:
                    value = value.strip('"').replace('_', ' ')

                setattr(self.my_model, key, value)
            self.my_model.save()

    def do_show(self, line):
        """ Prints the string representation of an instance
        based on the class name and id.
        Usage: how <ClassName> <id>
        """
        args = line.split()
        if not line:
            print("** class name missing **")
        elif args[0] not in our_models.keys():
            print("** class doesn't exist **")
        elif len(args) == 1:
            print("** instance id missing **")
        else:
            my_dict = storage.all()
            my_key = args[0] + '.' + args[1]
            if my_key in my_dict.keys():
                print(my_dict[my_key])
            else:
                print("** no instance found **")

    def do_all(self, line):
        """Prints all string representation of all instances
        based or not on the class name.
        Usage: all <ClassName> or all
        """
        out_all = []
        if not line:
            data = storage.all()
            for key, value in data.items():
                out_all.append(str(data[key]))
            print(out_all)
        elif line not in our_models.keys():
            print("** class doesn't exist **")
        else:
            data = storage.all()
            for key, value in data.items():
                class_name, obj_id = key.split('.')
                if line == class_name:
                    out_all.append(str(data[key]))
                else:
                    pass
            print(out_all)

    def do_destroy(self, line):
        """ deletes an instance based on the class name and id.
        Usage: destroy <ClassName> <id>
        """
        args = line.split()
        if not line:
            print("** class name missing **")
        elif args[0] not in our_models.keys():
            print("** class doesn't exist **")
        elif len(args) == 1:
            print("** instance id missing **")
        else:
            my_dict = storage.all()
            my_key = args[0] + '.' + args[1]
            if my_key in my_dict.keys():
                del my_dict[my_key]
                storage.save()
            else:
                print("** no instance found **")

    def do_update(self, line):
        """Updates an instance based on the class name and id
        Usage:
        update <class name> <id> <attribute name> "<attribute value>"
        """
        args = line.split()
        if not line:
            print("** class name missing **")
        elif args[0] not in our_models.keys():
            print("** class doesn't exist **")
        elif len(args) == 1:
            print("** instance id missing **")
        elif len(args) == 2:
            print("** attribute name missing **")
        elif len(args) == 3:
            print("** value missing **")
        else:
            storage.reload()
            my_dict = storage.all()
            my_key = args[0] + '.' + args[1]
            if my_key in my_dict.keys():
                try:
                    value = int(args[3])
                except ValueError:
                    value = args[3]
                setattr(my_dict[my_key], args[2], value)
                storage.save()

    def do_count(self, line):
        """Prints all string representation of all instances
        based or not on the class name.
        Ex: all <ClassName> or all
        """
        out_all = []
        if not line:
            data = storage.all()
            for key, value in data.items():
                out_all.append(str(data[key]))
            print(len(out_all))
        elif line not in our_models.keys():
            print("** class doesn't exist **")
        else:
            data = storage.all()
            for key, value in data.items():
                class_name, obj_id = key.split('.')
                if line == class_name:
                    out_all.append(str(data[key]))
                else:
                    pass
            print(len(out_all))

    # def precmd(self, line):
    #     """method used for splitting the line and convert it to
    #     keywords
    #     EX: User.all()
    #     all user
    #     """
    #     if "." in line:
    #         class_name, others = line.split(".")
    #         adv_func = ["all", "count", "show", "destroy"]
    #         func, attr = others.split("(")
    #         if (func in adv_func):
    #             line = func + " " + class_name + " " + attr[1:-2]
    #         else:
    #             id, name, value,  = attr.split(',')
    #             line = func + ' ' + class_name + ' ' + id[1:-1]  \
    #                 + ' ' + name[2:-1] + ' ' + value[:-1]
    #     return cmd.Cmd.precmd(self, line)


if __name__ == '__main__':
    HBNBCommand().cmdloop()
