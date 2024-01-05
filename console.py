#!/usr/bin/python3
"""Python Console"""

import cmd 
from datetime import datetime
import models
import re

class HBNBCommand(cmd.Cmd):
    """Class Console"""
    prompt = '(bnb)'
    
    def precmd(self, line):
        return line.strip()
    
    def do_EQF(self, line):
        """_summary_

        EQF:
            End of (_file_): _Exit console_
        """
        return True
    
    def do_quit(self, line):
        """_summary_

        quit :
            _exits the console_
        """
        
        return True
    
    def emptyline(self):
        pass
    
    def do_create(self, line):
        """_summary_

        create:
              
              Creates a new instance of BaseModel, saves it and prints the id
              
              If the class name is missing, return class missing
        """
        if len(line) == 0:
            print("** class name missing **")
        else:
            try:
                cls = models.class_dict(line)
            except KeyError:
                print("** class doesn't exist **")
            else:
                obj = cls()
                obj.save()
                print(obj.id)
                
    def do_show(self, line):
        """_summary_

        show:
            class name and id - print the string representation of an instance
            
            The method splits the arguments into smaller strings, 
            handles IndexError and KeyError, 
            and prints the result of class name and id to the screen.
        """
        if len(line) == 0:
            print("** class name missing **")
        else:
            pattern = "[^\s\"\']+|\"[^\"]*\"|\'[^\']*\'"
            pattern = re.compile(pattern)
            line = re.findall(pattern, line)
            for i in range(len(line)):
                line[i] = line[i].strip("\"'")
            if line[0] in models.class_dict:
                try:
                    obj_id = line[0] + '.' + line[1]
                except IndexError:
                    print("** instance id missing **")
                else:
                    try:
                        obj = models.storage.all()[obj_id]
                    except KeyError:
                        print("** no instance found **")
                    else:
                        try:
                            attr = line[2]
                        except IndexError:
                            print("** attribute name missing **")
                        else:
                            try:
                                val = line[3]
                            except IndexError:
                                print("** value missing **")
                            else:
                                try:
                                    setattr(obj, attr, val)
                                except AttributeError:
                                    print("** cannot set val: {}".format(val) +
                                          " for attr: ({}) **".format(attr))
                                else:
                                    obj.save()
            else:
                print("** class doesn't exist **")
                
    def do_count(self,line):
        """
        Usage: count [<class>]
        
        Count the num of instance of class if provided, else
        total num of instances in memory
        """
        if len(line) == 0:
            print(len([str(x) for x in models.storage.all().values()]))
        elif line not in models.class_dict:
            print("** class doesn't exist **")
        else:
            print(len([str(x) for x, y in models.storage.all().items()
                       if line in y]))
            
               
                    
    
    
if __name__ == '__main__':
    """command loop"""
    HBNBCommand().cmdloop()