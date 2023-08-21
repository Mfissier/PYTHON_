"""
    recyp : find_file
"""
import os
from utils.print.print_color import print_blue, print_green, print_red, print_yellow

def find_file(name, mod_dev = False):
#
    """
        Search and take path with filename
        ex: main.py return(/path/to/main.py)
        opt(mod_dev = True) for see diagnostic
    """
    if mod_dev is True :
        print_blue('Fun : find_file()')
    name = os.path.basename(name)
    path = os.path.dirname(os.path.join(os.getcwd(), ''))
    for root, dirs, files in os.walk(path) :
    #
        if mod_dev is True :
        #
            print_yellow(f'dirs : {dirs}')
            print_yellow(f'root : {root}')
            print_yellow(f'files : {files}')
        #
        if name in files:
        #
            if mod_dev is True :
            #
                print_green(f"\nResult path is :\n{os.path.join(root, name)}")
                print_blue('----------------')
            #
            return os.path.join(root, name)
        #
    #
    if mod_dev is True :
    #
        print_red('Path error | empty')
        print_blue('----------------')
    #
    return None
#
