import os

from utils.files.find_directory import find_directory
from utils.print.print_color import print_blue, print_green, print_red, print_yellow

def create_search_folder(folder_name, path_dir, mode_dev=False) :
#
    """Description
    Allows you to create a folder by specifying the path
    Args:
        folder_name (string): name of folder
        path_dir (string): The path where we will create the file
        mode_dev (bool, optional): True for see diagnostique
    Returns:
        string : the path of folder create or None if error
    """
    print_blue('Fun : create_search_folder')
    if path_dir is None :
    #
        if mode_dev is True :
            print_red('Error : path_dir is None')
        return None
    #
    if folder_name is None :
    #
        if mode_dev is True :
            print_red('Error : folder_name is None')
            return None
    #
    folder_name = os.path.basename(folder_name)
    path_dir = os.path.basename(path_dir)
    path_dir = find_directory(path_dir, mode_dev=mode_dev)
    if path_dir is None :
    #
        if mode_dev is True :
            print_red('Error : path_dir not found')
            return None
        return None
    #
    folder_name = os.path.join(path_dir, folder_name)
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
