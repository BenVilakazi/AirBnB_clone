#!/usr/bin/python3
"""Python Console"""

import cmd 
from datetime import datetime
import models
import re

class HBNBCommand(cmd.Cmd):
    pass
    
if __name__ == '__main__':
    """command loop"""
    HBNBCommand().cmdloop()