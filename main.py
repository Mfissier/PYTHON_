#!/usr/bin/env python
# -*- codage : utf-8 -*-
"""
    Main fun
"""
# from utils.files.check_update_file import check_update_file
from utils.files.create_dir import create_search_folder
from utils.files.create_file import create_search_file
from utils.files.find_directory import find_directory
from utils.files.find_file import check_file_is_clone, find_file
# from utils.syst_os.take_plateform import check_operating_system
# import time
from utils.syst_os.path import is_dir, is_file_search, path_default

def main() :
#
    """
    This main is juste for test
    """
    # print(find_file('test1.txt', './utils', mod_dev=True))
    # check_file_is_clone('path.py', mode_dev = True)
    # is_dir('/workspaces/PYTHON_', mode_dev = True)
    # is_file_search('path.py', mode_dev = True)
    # path_dir = find_directory("PYTHON_", mode_dev = True)
    # print(path_dir)
    create_search_folder("test", "./PYTHON_/utils", mode_dev=True)
    # find_directory()
    # create_search_file('test1.txt', "./utils", mode_dev=True)
#

if __name__ == "__main__":
    main()

