import os

from utils.files.find_directory import find_directory
from utils.print.print_color import print_blue, print_green, print_red, print_yellow

def create_search_dir(folder_name, path, mode_dev=False) :
#
    print_blue('Fun : create_search_dir')
    if path is None :
    #
        if mode_dev is True :
            print_red('Error : path is None')
        return None
    #
    if folder_name is None :
    #
        if mode_dev is True :
            print_red('Error : folder_name is None')
            return None
    #
    folder_name = os.path.basename(folder_name)
    path = os.path.basename(path)
    path = find_directory(path, mode_dev)
    if path is None :
    #
        if mode_dev is True :
            print_red('Error : Path not found')
            return None
        return None
    #
    folder_name = os.path.join(path, folder_name)
    try:
    #
        os.mkdir(folder_name)
        if mode_dev is True :
            print_yellow(f"Directory '{folder_name}' created successfully")
        return folder_name
    #
    except FileExistsError:
    #
        if mode_dev is True :
            print_red(f"Directory '{folder_name}' already exists")
        return None
    #
    except OSError as error:
    #
        if mode_dev is True :
        #
            print_red(f"Directory '{folder_name}' could not be created")
            print_red(f"Error: {error}")
        #
        return None
    #
#
