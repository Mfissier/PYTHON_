"""module os"""
import os

def path_default(path = None) :
#
    """
    Allows you to choose or not a default path. 
    If no path specified, it will be the path of the current repo,
    otherwise it will be the one given in parameter
    """
    if not path :
        path = os.getcwd()
    if not path.endswith(os.path.sep):
        path += os.path.sep
    return path
#
