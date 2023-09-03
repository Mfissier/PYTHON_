from utils.files.find_directory import find_directory
import os

from utils.print.print_color import print_yellow

def list_files(path, target_folder=None, mode_dev=False) :
#
    path = find_directory(path, target_folder=target_folder, mode_dev=mode_dev)
    if path == None :
        return None
    files_and_folders = os.listdir(path)
    return files_and_folders
#

def is_folder_empty(path, target_folder=None, mode_dev=False) :
#
    files_and_folders = list_files(path, target_folder=target_folder, mode_dev=mode_dev)
    if (files_and_folders == None) :
        return None
    elif (len(files_and_folders)) :
        return False
    return True
#

def list_all_folder(name, target_folder=None, mode_dev=False) :
#
    path = os.path.dirname(os.path.join(os.getcwd(), '../..'))
    name = os.path.basename(name)
    all_path = []
    count = 0
    for root, dir, files in os.walk(path) :
    #
        for elem in dir :
            if (os.path.normpath(os.path.join(root, elem)).find(name) != -1) :
                all_path.append(os.path.normpath(os.path.join(root, elem)))
                print_yellow(os.path.normpath(os.path.join(root, elem)))
        #
    #
    return all_path
#