"""module os"""
import os

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
            print_green(f'The path by default is false...')
            print_blue('---------------')
        return None
#
