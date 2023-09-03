
from utils.files.delete_file import rm_file
from utils.files.delete_folder import rm_dir
from utils.files.find_directory import find_directory
from utils.files.find_file import find_file
from utils.files.liste_files import is_folder_empty, list_all_folder, list_files
from utils.print.print_color import print_green, print_red, print_yellow


def all_filesDelete(path, target_folder=None, mode_dev=False) :
#
    """
        # Attempt to remove all files in the folder
        args :
            path (string) : path of folder
            target_folder (string /optional) : path of folder
            mode_dev (bool /optionnal) : True for see diagnostique
        return :
            path (string) or None if error
    """
    all_files = list_files(path, target_folder=target_folder, mode_dev=mode_dev)
    if (all_files is None) :
        return None
    for file in all_files :
        file = find_file(file, target_folder=path, mode_dev=mode_dev)
        if (file is not None) :
            rm_file(file, target_folder=path, mode_dev=mode_dev)
    return path
#

def forceDelete(path, target_folder=None, mode_dev=False) :
#
    """
        # Attempt to remove the file or the folder and all files in the folder
        args :
            path (string) : path of folder to delete
            target_folder (string /optional) : path of folder
            mode_dev (bool /optionnal) : True for see diagnostique
        return :
            path (string) or None if error
    """
    find_path_folder = find_directory(path, target_folder=target_folder, mode_dev=mode_dev)
    find_path_file = find_file(path, target_folder=target_folder, mode_dev=mode_dev)
    if (find_path_folder is not None and find_path_file is not None) :
    #
        if mode_dev is True :
            print_red('Need to choose between the file and the folder')
            print_red('user target_folder for make a choice')
        return None
    #
    if (find_path_folder is not None) :
    #
        if is_folder_empty(find_path_folder, target_folder=target_folder, mode_dev=mode_dev) :
        # 
            rm_dir(find_path_folder, target_folder=target_folder, mode_dev=mode_dev)
        # 
        else :
        # 
            all_folder = list_all_folder(find_path_folder, target_folder=target_folder, mode_dev=mode_dev)
            all_folder.reverse()
            for elem in all_folder :
            # 
                all_filesDelete(elem, target_folder=path, mode_dev=mode_dev)
                if rm_dir(elem, target_folder=path, mode_dev=mode_dev) == None :
                #
                    if mode_dev is True :
                        print_red(f'Error when deleting the folder or files:\n{elem}') 
                    return None
                #
            #
            if mode_dev is True :
                print_green(f'The folder and more path is delete :\n{all_folder}')
            return all_folder
        #
    #
    elif (find_path_file is not None) :
    #
        if rm_file(find_path_file, target_folder=target_folder, mode_dev=mode_dev) == None :
        #
            if mode_dev is True :
                print_red(f'Error when deleting the file :\n{find_path_file}') 
            return None
        #
        return find_path_file
    #
    else :
    #
        if mode_dev is True :
            print_red('Detect file or folder failed')
        return None
    #
#