from utils.files.find_file import find_file
from utils.print.print_color import print_blue, print_red


def write_in_file(file, content, target_folder=None, mode_dev=False) :
#
    """
        Write in file
        args :
            file (string): name of file
            content (string): content to write in file
            target_folder (string): folder where to search file
            mode_dev (bool): if True, print diagnostique
        return :
            True if success or false if not
        exept :
            if file not found or file is clone in the folder
        exemple :
            write_in_file('path/test1.txt', 'content', target_folder='PYTHON_', mode_dev=True)
    """
    if mode_dev is True :
        print_blue('fun : write_in_file')
    path_file = find_file(file, target_folder=target_folder, mode_dev=mode_dev)
    if path_file :
    #
        try:
        #
            with open(path_file, 'w') as file:
            #
                file.write(content)
            #
            return True
        #
        except FileNotFoundError:
        #
            if mode_dev is True :
                print_red("The file was not found.")
            return False
        #
        except PermissionError:
        #
            if mode_dev is True :
                print_red("Permission denied when attempting to open the file.")
            return False
        #
        except Exception as e:
        #
            if mode_dev is True :
                print_red(f"An error occurred: {e}")
            return False
    #
    return False
#