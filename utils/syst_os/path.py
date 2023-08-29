"""module os"""
import os
from utils.files.find_file import find_file
"""module os"""
import os
from utils.print.print_color import print_blue, print_green, print_red, print_yellow
from pathlib import Path
from utils.print.print_color import print_blue, print_green

def is_valid_path(path) :
#
    """Check if the path exists on the current system"""
    return (os.path.exists(path))
#

def path_default(path = None, mode_dev = False) :
#
    """
    Allows you to choose or not a default path. 
    If no path specified, it will be the path of the current project repo,
    otherwise it will be the one given in parameter
    """
    if mode_dev :
        print_blue('fun : path_default')
    if not path :
        path = os.getcwd()
    if not path.endswith(os.path.sep):
        path += os.path.sep
    if is_valid_path(path) :
        if mode_dev :
            print_green(f'The path by default is : {path}' )
            print_blue('---------------')
        return path
    else :
        if mode_dev :
            print_green('The path by default is false...')
            print_blue('---------------')
        return None
#

def is_dir(path, mode_dev = False) :
#
    """Determines if the path points to a folder"""
    if mode_dev is True :
        print_blue('Fun : is_dir()')
    if Path(path).is_dir() is True :
    #
        if mode_dev is True :
            print_yellow(f'Path : {path}  | is dir [True]')
        return (True)
    #
    else : 
    #
        if mode_dev is True :
            print_yellow(f'Path : {path}  | is not a dir [False]')
        return (False)
    #
#

def is_file_search(path, mode_dev = False) :
#
    """Determines if the path points to a file"""
    if mode_dev is True :
        print_blue('Fun : is_file()')
    path = find_file(path, mode_dev)
    if path is None :
    #
        if mode_dev is True :
            print_red('Path error, setting -> [None]...')
        return None
    #
    if Path(path).is_file() is True :
    #
        if mode_dev is True :
            print_yellow(f'Path : {path}  | is file [True]')
        return True
    #
    else :
    #
        if mode_dev is True :
            print_yellow(f'Path : {path}  | is not a file [False]')
        return False
    #
#
