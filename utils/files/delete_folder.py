import os
from utils.files.find_directory import find_directory
from utils.print.print_color import print_blue, print_green, print_red, print_yellow

def rm_dir(folder, target_folder=None, mode_dev=False) :
#
    """
        # Attempt to remove the file
        args :
            folder (string)
            target_folder (string /optional)
            mode_dev (bool /optionnal)
        return :
            folder_path (string) or None if error
        exept :
            if file not found or file is clone in the folder
        exemple :
            rm_dir('test', target_folder='PYTHON_', mode_dev=True)
            # delete the folder test in the folder PYTHON_
    """
    if mode_dev is True :
        print_blue('fun : rm_dir')
    folder_path = find_directory(folder, target_folder=target_folder, mode_dev=mode_dev)
    if folder_path :
    #
        try:
        #
            os.rmdir(folder_path)
            if mode_dev is True :
                print_green(f"The file '{folder_path}' has been successfully deleted.")
            return folder_path
        #
        except OSError as e:
        #
            if mode_dev is True :
                print_red(f"An error occurred while deleting the folder '{folder_path}':\n{e}")
            return None
        #
    #
    if mode_dev is True :
        print_red("The folder does not exist.")
    return None
#