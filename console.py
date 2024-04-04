#!/usr/bin/python3
<<<<<<< HEAD

"""
Console Module
"""
import cmd
=======
""" Console Module """
import cmd
import sys
>>>>>>> a9fe34ecaf215ca72d84256baacbc86bc6faa8cd
from models.base_model import BaseModel
from models.__init__ import storage
from models.user import User
from models.place import Place
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.review import Review


class HBNBCommand(cmd.Cmd):
    """ Contains the functionality for the HBNB console"""
<<<<<<< HEAD
    # determines prompt for interactive/non-interactive modes
    prompt = '(hbnb) '  # if sys.__stdin__.isatty() else ''
=======

    # determines prompt for interactive/non-interactive modes
    prompt = '(hbnb) ' if sys.__stdin__.isatty() else ''
>>>>>>> a9fe34ecaf215ca72d84256baacbc86bc6faa8cd

    classes = {
               'BaseModel': BaseModel, 'User': User, 'Place': Place,
               'State': State, 'City': City, 'Amenity': Amenity,
               'Review': Review
              }
    dot_cmds = ['all', 'count', 'show', 'destroy', 'update']
    types = {
             'number_rooms': int, 'number_bathrooms': int,
             'max_guest': int, 'price_by_night': int,
             'latitude': float, 'longitude': float
            }

<<<<<<< HEAD
    # def preloop(self):
    #    """Prints if isatty is false"""
    #    if not sys.__stdin__.isatty():
    #        print('(hbnb) ', end='')
=======
    def preloop(self):
        """Prints if isatty is false"""
        if not sys.__stdin__.isatty():
            print('(hbnb)')
>>>>>>> a9fe34ecaf215ca72d84256baacbc86bc6faa8cd

    def precmd(self, line):
        """Reformat command line for advanced command syntax.

        Usage: <class name>.<command>([<id> [<*args> or <**kwargs>]])
        (Brackets denote optional fields in usage example.)
        """
        _cmd = _cls = _id = _args = ''  # initialize line elements

        # scan for general formating - i.e '.', '(', ')'
        if not ('.' in line and '(' in line and ')' in line):
            return line

        try:  # parse line left to right
            pline = line[:]  # parsed line

            # isolate <class name>
            _cls = pline[:pline.find('.')]

            # isolate and validate <command>
            _cmd = pline[pline.find('.') + 1:pline.find('(')]
            if _cmd not in HBNBCommand.dot_cmds:
                raise Exception

            # if parantheses contain arguments, parse them
            pline = pline[pline.find('(') + 1:pline.find(')')]
            if pline:
                # partition args: (<id>, [<delim>], [<*args>])
                pline = pline.partition(', ')  # pline convert to tuple

                # isolate _id, stripping quotes
                _id = pline[0].replace('\"', '')
                # possible bug here:
                # empty quotes register as empty _id when replaced

                # if arguments exist beyond _id
                pline = pline[2].strip()  # pline is now str
                if pline:
                    # check for *args or **kwargs
                    if pline[0] == '{' and pline[-1] == '}'\
                            and type(eval(pline)) is dict:
                        _args = pline
                    else:
                        _args = pline.replace(',', '')
                        # _args = _args.replace('\"', '')
            line = ' '.join([_cmd, _cls, _id, _args])

<<<<<<< HEAD
        except Exception:
=======
        except Exception as mess:
>>>>>>> a9fe34ecaf215ca72d84256baacbc86bc6faa8cd
            pass
        finally:
            return line

    def postcmd(self, stop, line):
        """Prints if isatty is false"""
<<<<<<< HEAD
        # if not sys.__stdin__.isatty():
        #    print('(hbnb) ')
        return stop

    def postloop(self):
        """end on a newline"""
        # print()

    def do_quit(self, command):
        """ Method to exit the HBNB console"""
        return True
=======
        if not sys.__stdin__.isatty():
            print('(hbnb) ', end='')
        return stop

    def do_quit(self, command):
        """ Method to exit the HBNB console"""
        exit()
>>>>>>> a9fe34ecaf215ca72d84256baacbc86bc6faa8cd

    def help_quit(self):
        """ Prints the help documentation for quit  """
        print("Exits the program with formatting\n")

    def do_EOF(self, arg):
        """ Handles EOF to exit program """
        print()
<<<<<<< HEAD
        return True
=======
        exit()
>>>>>>> a9fe34ecaf215ca72d84256baacbc86bc6faa8cd

    def help_EOF(self):
        """ Prints the help documentation for EOF """
        print("Exits the program without formatting\n")

    def emptyline(self):
        """ Overrides the emptyline method of CMD """
        pass

    def do_create(self, args):
        """ Create an object of any class"""
<<<<<<< HEAD
        params = self.__validateArgs(args)
        if type(params) != dict:
            return
        try:
            new_instance = HBNBCommand.classes[args.split()[0]](**params)
            # [setattr(new_instance, k, v) for k, v in params.items()]
            new_instance.save()
            print(new_instance.id)
        except Exception:
            pass

    def __validateArgs(self, args):
        """Validates Input arguments"""
        if not args:
            return print("** class name missing **")
        args = args.split()
        if args[0] not in self.classes:
            return print("** class doesn't exist **")
        params = {}
        for arg in args[1:]:
            param = arg.split('=')
            if len(param) == 2:
                value = param[1]
                if value[0] == '"' and value[-1] == '"':
                    params[param[0]] = value.replace('_', ' ').strip('"')
                elif value.isnumeric():
                    params[param[0]] = int(value)
                else:
                    try:
                        if float(value):
                            params[param[0]] = float(value)
                    except Exception:
                        pass
        return params
=======
        try:
            if not args:
                raise SyntaxError()
            arg_list = args.split(" ")
            kw = {}
            for arg in arg_list[1:]:
                arg_splited = arg.split("=")
                arg_splited[1] = eval(arg_splited[1])
                if type(arg_splited[1]) is str:
                    arg_splited[1] = arg_splited[1].replace("_", " ").replace('"', '\\"')
                kw[arg_splited[0]] = arg_splited[1]
        except SyntaxError:
            print("** class name missing **")
        except NameError:
            print("** class doesn't exist **")
        new_instance = HBNBCommand.classes[arg_list[0]](**kw)
        new_instance.save()
        print(new_instance.id)
>>>>>>> a9fe34ecaf215ca72d84256baacbc86bc6faa8cd

    def help_create(self):
        """ Help information for the create method """
        print("Creates a class of any type")
        print("[Usage]: create <className>\n")

    def do_show(self, args):
        """ Method to show an individual object """
        new = args.partition(" ")
        c_name = new[0]
        c_id = new[2]
<<<<<<< HEAD
        # guard against trailing args
        if c_id and ' ' in c_id:
            c_id = c_id.partition(' ')[0]
        if not c_name:
            return print("** class name missing **")
        if c_name not in HBNBCommand.classes:
            return print("** class doesn't exist **")
        if not c_id:
            return print("** instance id missing **")
        objs = storage.all(c_name).values()
        obj = [v for v in objs if v.id == c_id]
        print("** no instance found **") if len(obj) == 0 else print(obj[0])
=======

        # guard against trailing args
        if c_id and ' ' in c_id:
            c_id = c_id.partition(' ')[0]

        if not c_name:
            print("** class name missing **")
            return

        if c_name not in HBNBCommand.classes:
            print("** class doesn't exist **")
            return

        if not c_id:
            print("** instance id missing **")
            return

        key = c_name + "." + c_id
        try:
            print(storage._FileStorage__objects[key])
        except KeyError:
            print("** no instance found **")
>>>>>>> a9fe34ecaf215ca72d84256baacbc86bc6faa8cd

    def help_show(self):
        """ Help information for the show command """
        print("Shows an individual instance of a class")
        print("[Usage]: show <className> <objectId>\n")

    def do_destroy(self, args):
        """ Destroys a specified object """
        new = args.partition(" ")
        c_name = new[0]
        c_id = new[2]
        if c_id and ' ' in c_id:
            c_id = c_id.partition(' ')[0]
<<<<<<< HEAD
        if not c_name:
            return print("** class name missing **")
        if c_name not in HBNBCommand.classes:
            return print("** class doesn't exist **")
        if not c_id:
            return print("** instance id missing **")
        objs = storage.all(c_name).values()
        obj = [v for v in objs if v.id == c_id]
        print("** no instance found **") if len(obj) == 0 else obj[0].delete()
=======

        if not c_name:
            print("** class name missing **")
            return

        if c_name not in HBNBCommand.classes:
            print("** class doesn't exist **")
            return

        if not c_id:
            print("** instance id missing **")
            return

        key = c_name + "." + c_id

        try:
            del(storage.all()[key])
            storage.save()
        except KeyError:
            print("** no instance found **")
>>>>>>> a9fe34ecaf215ca72d84256baacbc86bc6faa8cd

    def help_destroy(self):
        """ Help information for the destroy command """
        print("Destroys an individual instance of a class")
        print("[Usage]: destroy <className> <objectId>\n")

    def do_all(self, args):
        """ Shows all objects, or all objects of a class"""
<<<<<<< HEAD
        cls = None
        if args:
            cls = args.split(' ')[0]  # remove possible trailing args
            if cls not in HBNBCommand.classes:
                return print("** class doesn't exist **")
        from models import storage
        objs = storage.all(cls)
        print([str(v) for v in objs.values()])
=======
        print_list = []

        if args:
            args = args.split(' ')[0]  # remove possible trailing args
            if args not in HBNBCommand.classes:
                print("** class doesn't exist **")
                return
            for k, v in storage.all(HBNBCommand.classes[args]).items():
                print_list.append(str(v))
        else:
            for k, v in storage.all().items():
                print_list.append(str(v))
        print(print_list)
>>>>>>> a9fe34ecaf215ca72d84256baacbc86bc6faa8cd

    def help_all(self):
        """ Help information for the all command """
        print("Shows all objects, or all of a class")
        print("[Usage]: all <className>\n")

    def do_count(self, args):
        """Count current number of class instances"""
<<<<<<< HEAD
        if args not in self.classes:
            return print("** class doesn't exist **")
        print(len(storage.all(args).values()))
=======
        count = 0
        for k, v in storage._FileStorage__objects.items():
            if args == k.split('.')[0]:
                count += 1
        print(count)
>>>>>>> a9fe34ecaf215ca72d84256baacbc86bc6faa8cd

    def help_count(self):
        """ """
        print("Usage: count <class_name>")

    def do_update(self, args):
        """ Updates a certain object with new info """
        c_name = c_id = att_name = att_val = kwargs = ''

        # isolate cls from id/args, ex: (<cls>, delim, <id/args>)
        args = args.partition(" ")
        if args[0]:
            c_name = args[0]
        else:  # class name not present
            print("** class name missing **")
            return
        if c_name not in HBNBCommand.classes:  # class name invalid
            print("** class doesn't exist **")
            return

        # isolate id from args
        args = args[2].partition(" ")
        if args[0]:
            c_id = args[0]
        else:  # id not present
            print("** instance id missing **")
            return

        # generate key from class and id
        key = c_name + "." + c_id

        # determine if key is present
<<<<<<< HEAD
        if key not in storage.all(c_name):
=======
        if key not in storage.all():
>>>>>>> a9fe34ecaf215ca72d84256baacbc86bc6faa8cd
            print("** no instance found **")
            return

        # first determine if kwargs or args
        if '{' in args[2] and '}' in args[2] and type(eval(args[2])) is dict:
            kwargs = eval(args[2])
            args = []  # reformat kwargs into list, ex: [<name>, <value>, ...]
            for k, v in kwargs.items():
                args.append(k)
                args.append(v)
        else:  # isolate args
            args = args[2]
            if args and args[0] == '\"':  # check for quoted arg
                second_quote = args.find('\"', 1)
                att_name = args[1:second_quote]
                args = args[second_quote + 1:]

            args = args.partition(' ')

            # if att_name was not quoted arg
            if not att_name and args[0] != ' ':
                att_name = args[0]
            # check for quoted val arg
            if args[2] and args[2][0] == '\"':
                att_val = args[2][1:args[2].find('\"', 1)]

            # if att_val was not quoted arg
            if not att_val and args[2]:
                att_val = args[2].partition(' ')[0]

            args = [att_name, att_val]

        # retrieve dictionary of current objects
<<<<<<< HEAD
        new_dict = storage.all(c_name)[key]
=======
        new_dict = storage.all()[key]
>>>>>>> a9fe34ecaf215ca72d84256baacbc86bc6faa8cd

        # iterate through attr names and values
        for i, att_name in enumerate(args):
            # block only runs on even iterations
            if (i % 2 == 0):
                att_val = args[i + 1]  # following item is value
                if not att_name:  # check for att_name
                    print("** attribute name missing **")
                    return
                if not att_val:  # check for att_value
                    print("** value missing **")
                    return
                # type cast as necessary
                if att_name in HBNBCommand.types:
                    att_val = HBNBCommand.types[att_name](att_val)

                # update dictionary with name, value pair
                new_dict.__dict__.update({att_name: att_val})

        new_dict.save()  # save updates to file

    def help_update(self):
        """ Help information for the update class """
        print("Updates an object with new information")
        print("Usage: update <className> <id> <attName> <attVal>\n")

<<<<<<< HEAD

=======
>>>>>>> a9fe34ecaf215ca72d84256baacbc86bc6faa8cd
if __name__ == "__main__":
    HBNBCommand().cmdloop()
