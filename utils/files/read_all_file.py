from utils.files.find_file import find_file
from utils.print.print_color import print_blue, print_green, print_red, print_yellow

def read_no_error(path, mode_dev=False) :
#
    """
        Read file
        args :
            path (string): path of file
            mode_dev (bool): if True, print diagnostique
        return :
            content of file or None if error
        exept :
            if file not found or file is clone in the folder
        exemple :
            read_no_error('path/test.txt', mode_dev=True)
            # read the file test.txt
    """
    all_lines = ""
    if mode_dev is True :
        print_blue('fun : read_no_error')
    try:
    #
        with open(path, 'r') as file:
        #
            content = file.read()
            all_lines += content
        #
    #
    except FileNotFoundError:
    #
        if mode_dev is True :
            print_red("The file was not found.")
        return None
    #
    except PermissionError:
    #
        if mode_dev is True :
            print_red("Permission denied when attempting to open the file.")
        return None
    #
    except Exception as e:
    #
        if mode_dev is True :
            print_red(f"An error occurred: {e}")
        return None
    #
    if mode_dev is True :
        print_green(f"File '{path}' read successfully")
    return all_lines
#

def readfile_to_str(file, target_folder=None, mode_dev=False) :
#
    """
        Read file
        args :
            file (string): name of file
            target_folder (string): folder where to search file
            mode_dev (bool): if True, print diagnostique
        return :
            content of file or None if error
        exept :
            if file not found or file is clone in the folder
        exemple :
            readfile_to_str('path/test.txt', target_folder='PYTHON_', mode_dev=True)
            # read the file test.txt in the folder PYTHON_
    """
    if mode_dev is True :
        print_blue('fun : readfile_to_str')
    content = ""
    path_file = find_file(file, target_folder=target_folder, mode_dev=mode_dev)
    if path_file :
    #
        content = read_no_error(path_file, mode_dev=mode_dev)
        if content is None :
            return None
        return content
    #
    else :
        return None
#

def readfile_to_json(file, target_folder=None, mode_dev=False) :
#
    """
        Read file and convert to json
        args :
            file (string): name of file
            target_folder (string): folder where to search file
            mode_dev (bool): if True, print diagnostique
        return :
            content of file or None if error
        exept :
            if file not found or file is clone in the folder
        exemple :
            readfile_to_json('path/test.json', target_folder='PYTHON_', mode_dev=True)
            # read the file test.json in the folder PYTHON_ and convert to json
    """
    if mode_dev is True :
        print_blue('fun : readfile_to_str')
    content = ""
    path_file = find_file(file, target_folder=target_folder, mode_dev=mode_dev)
    if path_file :
    #
        content = read_no_error(path_file, mode_dev=mode_dev)
        if content is None :
            return None
        return content
    #
    else :
        return None
#