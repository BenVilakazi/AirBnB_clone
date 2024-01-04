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

        Args:
        quit : _exits the console_
        """
        
        return True
    
    def emptyline(self):
        pass
    
    def do_create(self, line):
        pass
    
    
    
if __name__ == '__main__':
    """command loop"""
    HBNBCommand().cmdloop()