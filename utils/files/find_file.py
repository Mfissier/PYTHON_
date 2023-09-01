"""
    recyp : find_file, check_file_is_clone
"""
import os
from utils.print.print_color import print_blue, print_green, print_red, print_yellow

def check_file_is_clone(name, mode_dev=False) :
#
    """
        Checks if the file is in several copies from the program execution directory
    """
    path = os.path.dirname(os.path.join(os.getcwd(), ''))
    name = os.path.basename(name)
    count = 0
    all_path = []
    if mode_dev is True :
        print_blue('Fun : check_file_is_clone()')
    for root, dir, files in os.walk(path) :
    #
        for elem in files :
        #
            # print(os.path.join(root, elem)) # for see all path
            if name in elem:
            #
                all_path.append(os.path.join(root, name))
                count += 1
            #
        #
    #
    if count > 1 :
    #
        if mode_dev is True :
        #
            print_yellow(f'The file as been cloned :\n{all_path}')
            print_blue('<------------------------')
        #
        return True
    #
    if mode_dev is True :
        print_yellow('The file is unique')
    return False
#

def find_file(name, mod_dev = False):
#
    """
        Search and take path with filename
        ex: main.py return(main.py)
        opt(mod_dev = True) for see diagnostic
    """
    if mod_dev is True :
        print_blue('Fun : find_file()')
    if name is None :
    #
        if mod_dev is True :
            print_red('Var name is None')
        return None
    #
    name = os.path.basename(name)
    path = os.path.dirname(os.path.join(os.getcwd(), ''))
    if (check_file_is_clone(name, mod_dev) is True) :
    #
        if mod_dev is True :
        #
            print_red('A potential error has been found. \n' +
                      'The search file exists in several copies.')
            print_blue('<------------------------')
        #
        return (None)
    #
    for root, dir, files in os.walk(path) :
    #
        for elem in files :
        # 
            if name in elem :
            #
                if mod_dev is True :
                #
                    print_green(f"Result path is :\n{os.path.join(root, name)}")
                    print_blue('----------------')
                #
                return os.path.join(root, name)
            #
        #
    #
    if mod_dev is True :
    #
        print_red('The path was not found')
        print_blue('----------------')
    #
    return None
#
