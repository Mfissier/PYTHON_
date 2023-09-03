
from utils.files.find_directory import find_directory
from utils.files.find_file import find_file
from utils.print.print_color import print_red, print_yellow



def rm_rf(path, target_folder=None, mode_dev=False) :
#
    find_path_folder = find_directory(path, target_folder=target_folder, mode_dev=mode_dev)
    find_path_file = find_file(path, target_folder=target_folder, mode_dev=mode_dev)
    if (find_path_folder is not None and find_path_file is not None) :
    #
        print_red('Need to choose between the file and the folder')
        print_red('user target_folder for make a choice')
        return None
    #
    if (find_path_folder is not None) :
    #
        print_yellow('The folder is found')
    #
    elif (find_path_file is not None) :
    #
        print_yellow('The file is found')
    #
    else :
    #
        print_red('Detect file or folder failed')
    #
    return None
#