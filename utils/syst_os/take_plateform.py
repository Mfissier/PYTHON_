#!/usr/bin/env python
# -*- codage : utf-8 -*-
"""
    Import time...
"""
import os
from utils.print.print_color import print_blue, print_green

def check_operating_system(mod_dev = False) :
#
    """ 
    Return name of operating system
    opt(mod_dev = True) for see diagnostic
    """
    if mod_dev is True :
        print_blue('Fun : check_operating_system()')
    #-------------------------------
    if os.name == 'posix' :
        if mod_dev is True :
            print_green('Result : Linux or MacOs')
    elif os.name == 'nt':
        if mod_dev is True :
            print_green('Result : Windows')
    elif os.name == 'java' :
        if mod_dev is True :
            print_green('Result : Jython environment')
    else:
        if mod_dev is True :
            print_green(f"Rsult : Unrecognized platform: {os.name}")
    if mod_dev :
        print_blue('----------------')
    return os.name
#
