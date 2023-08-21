import os
from termcolor import colored
from utils.print.print_error import print_error

def find_file(name):
#
    name = os.path.basename(name)
    path = os.path.dirname(os.path.join(os.getcwd(), ''))

    for root, dirs, files in os.walk(path) :
    #
        if name in files:
            return os.path.join(root, name)
    #
    return (None)
#

# #
# Allows to search from the execution path of the program a file
# #