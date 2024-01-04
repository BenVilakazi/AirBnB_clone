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
            
            
        """
    
    
    
if __name__ == '__main__':
    """command loop"""
    HBNBCommand().cmdloop()