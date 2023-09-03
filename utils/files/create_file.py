import os
from utils.files.find_directory import find_directory
from utils.files.find_file import find_file
from utils.print.print_color import print_blue, print_green, print_red, print_yellow

def create_search_file(file_name, path_dir, mode_dev=False) :
#
    """Description
    Allows you to create a folder by specifying the path
    Args:
        file_name (string): name of file
        path_dir (string): the path directory for create a file
        mode_dev (bool, optional): True for see diagnostique
    Returns:
        string : the path of file create or None if error
    """

    print_blue('Fun : create_search_file')
    if path_dir is None :
    #
        if mode_dev is True :
            print_red('Error : path_dir is None')
        return None
    #
    if file_name is None :
    #
        if mode_dev is True :
            print_red('Error : file_name is None')
            return None
    #
    file_name = os.path.basename(file_name)
    path_dir = os.path.basename(path_dir)
    path_dir = find_directory(path_dir, mode_dev=mode_dev)
    if path_dir is None :
    #
        if mode_dev is True :
            print_red('Error : path_dir not found')
            return None
        return None
    #
    file_name = os.path.join(path_dir, file_name)
    try:
    #
        os.mknod(file_name)
        if mode_dev is True :
            print_yellow(f"File '{file_name}' created successfully")
        return file_name
    #
    except FileExistsError:
    #
        if mode_dev is True :
            print_red(f"File '{file_name}' already exists")
        return None
    #
    except OSError as error:
    #
        if mode_dev is True :
        #
            print_red(f"File '{file_name}' could not be created")
            print_red(f"Error: {error}")
        #
        return None
    #
#
