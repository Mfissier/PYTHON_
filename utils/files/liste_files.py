from utils.files.find_directory import find_directory
import os

from utils.print.print_color import print_blue, print_green, print_yellow

def list_files(path, target_folder=None, mode_dev=False) :
#
    """
        # Attempt to list the files in the folder
        args :
            path (string) : path of folder
            target_folder (string /optional) : path of folder
            mode_dev (bool /optionnal) : True for see diagnostique
        return :
            files_and_folders (list) or None if error
    """
    if mode_dev is True :
        print_blue('Fun : list_files()')
    path = find_directory(path, target_folder=target_folder, mode_dev=mode_dev)
    if path == None :
        return None
    files_and_folders = os.listdir(path)
    if mode_dev is True :
        print_green(f'List of files in folder :\n{files_and_folders}')
    return files_and_folders
#

def is_folder_empty(path, target_folder=None, mode_dev=False) :
#
    """
        # Check if the folder is empty
        args :
            path (string) : path of folder
            target_folder (string /optional) : path of folder
            mode_dev (bool /optionnal) : True for see diagnostique
        return :
            True if folder is empty
    """
    if mode_dev is True :
        print_blue('Fun : is_folder_empty()')
    files_and_folders = list_files(path, target_folder=target_folder, mode_dev=mode_dev)
    if (files_and_folders == None) :
        return None
    elif (len(files_and_folders)) :
    #
        if mode_dev is True :
            print_green('The folder is not empty')
        return False
    #
    if mode_dev is True :
        print_green('The folder is empty')
    return True
#

def list_all_folder(name, target_folder=None, mode_dev=False) :
#
    """
        list all folder with path absolute
        args :
            name (string) : name of folder for search
            target_folder (string /optional) : path of folder
            mode_dev (bool /optionnal) : True for see diagnostique
        return :
            all_path (list) : list path of folder
    """
    if mode_dev is True :
        print_blue('Fun : list_all_folder()')
    path = os.path.dirname(os.path.join(os.getcwd(), '../..'))
    name = os.path.basename(name)
    all_path = []
    count = 0
    for root, dir, files in os.walk(path) :
    #
        for elem in dir :
            if (os.path.normpath(os.path.join(root, elem)).find(name) != -1) :
                all_path.append(os.path.normpath(os.path.join(root, elem)))
        #
    #
    if mode_dev is True :
    #
        print_green('List of all folder :')
        print_green(os.path.normpath(os.path.join(root, elem)))
    #
    return all_path
#