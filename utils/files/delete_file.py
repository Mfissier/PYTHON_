import os
from utils.files.find_file import find_file
from utils.print.print_color import print_blue, print_red, print_yellow

def rm_file(file, target_folder=None, mode_dev=False) :
#
    """
        # Attempt to remove the file
        args :
            file (string)
            target_file (string /optional)
            mode_dev (bool /optionnal)
        return :
            file_path (string) or None if error
    """
    if mode_dev is True :
        print_blue('fun : rm_dir')
    file_path = find_file(file, target_folder=target_folder, mode_dev=mode_dev)
    if file_path :
    #
        try:
        #
            os.remove(file_path)
            if mode_dev is True :
                print_yellow(f"The file '{file_path}' has been successfully deleted.")
            return file_path
        #
        except OSError as e:
        #
            if mode_dev is True :
                print_red(f"An error occurred while deleting the file '{file_path}': {e}")
            return None
        #
    #
    if mode_dev is True :
        print_red("The file does not exist.")
    return None
#