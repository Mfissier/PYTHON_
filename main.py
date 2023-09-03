#!/usr/bin/env python
# -*- codage : utf-8 -*-
"""
    Main fun
"""
# from utils.files.check_update_file import check_update_file
from utils.files.create_dir import create_search_folder
from utils.files.create_file import create_search_file
from utils.files.delete_folder import rm_dir
from utils.files.find_directory import check_folder_is_clone, find_directory
from utils.files.find_file import check_file_is_clone, find_file
from utils.files.liste_files import is_folder_empty, list_all_folder, list_files
from utils.files.rm_rf import forceDelete
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
    # create_search_folder("test", "./PYTHON_/utils", mode_dev=True)
    # find_directory()
    
    # print(find_file("print_error.py", mod_dev=True))
    # create_search_file('test1.txt', "./utils", mode_dev=True)
    # rm_file('test', mode_dev=True)
    # find_directory('LAA', target_folder='CCCC',mode_dev=True)
    # rm_dir('test', mode_dev=True)
    # print(is_folder_empty('CCCC', mode_dev=False))
    # list_all_folder(find_directory('CCCC'), mode_dev=True)
    forceDelete('test_rm', mode_dev=True)
    # find_file('test1.txt', target_folder='PYTHON_', mode_dev=True)
#

if __name__ == "__main__":
    main()
