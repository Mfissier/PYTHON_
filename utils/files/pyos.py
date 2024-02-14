"""
    Library for file management
    content :
        create_json_file(data, file_name, mode_dev=False)
        files_time_modified(filepath)
        check_update_file(filename, target_folder=None)
        create_search_folder(folder_name, path_dir)
        create_search_file(file_name, path_dir)
        rm_file(file, target_folder=None)
        rm_filesdir(path, target_folder=None)
        rm_dir(folder, target_folder=None)
        rm_force(path, target_folder=None)
        check_file_is_clone(name, target_folder=None)
        find_file(name, target_folder = None )
        check_folder_is_clone(name, target_folder=None)
        find_folder(name,  target_folder=None)
        ls_files(path, target_folder=None)
        ls_allfolder(name, target_folder=None)
        is_folder_empty(path, target_folder=None)
        read_no_error(path)
        readfile_to_str(file, target_folder=None)
        readfile_to_json(file, target_folder=None)
        is_valid_path(path)
        path_default(path = None, mode_dev = False)
        is_dir(path, mode_dev = False)
        check_operating_system(mod_dev = False)
        is_folder_exist(folder, target_folder=None)
        is_file_search(path, mode_dev = False)
    
    comment :
        This module is a library for file management and dev more easely
        This library will facilitate development when you want to manage an environment with python.
        It is imperative to check that the files, folder, create are not the same names.
        Of course, it is always possible to focus on a particular folder. 
        This constraint forces you to choose carefully the way you organize your rest and, 
        above all, to make path management more understandable.

        Each function has a description and usage examples.
        In addition, mode_dev allows you to see possible errors in depth, if you need in-depth debugging

    dependance :
        Python 3.8.10 (default, May 26 2023, 14:05:08) | os | datetime | pylint 
"""

import os
import json
import datetime
from pathlib import Path
from utils.print.print_color import print_blue, print_green, print_red, print_yellow

class file :
#
    """class static for save status of file check"""
    rec_time = 0
    new_time = 0

    @staticmethod
    def get_rec_time() :
        """Change var file.rec_time"""
        return file.rec_time

    @staticmethod
    def change_rec_time(time) :
    #
        """Change var file.rec_time"""
        file.rec_time = time
        return time
    #

    @staticmethod
    def get_new_time() :
        """Get file.new_time"""
        return(file.new_time)

    @staticmethod
    def change_new_time(time) :
    #
        """Get file.new_time"""
        file.new_time = time
        return (time)
    #
#

def create_json_file(data, file_name, mode_dev=False) :
#
    """
        Create a json file with data
        args :
            data (dict) : data for save in json file
            file_name (string) : name of file
            mode_dev (bool /optionnal) : True for see diagnostique
        return :
            None if error
        exemple :
            create_json_file(data, 'test.json', mode_dev=True)
            # create the file test.json with data
    """
    if data is None :
    #
        if mode_dev :
            print_red('Error : data is None')
        return None
    #
    if file_name is None :
    #
        if mode_dev :
            print_red('Error : file_name is None')
        return None
    try:
    #
        with open(file_name, "w") as json_file:
            json.dump(data, json_file, indent=4)
        if mode_dev :
            print_yellow(f"JSON data has been successfully saved to {file_name}")
    #
    except FileNotFoundError:
    #
        print(f"Error: File '{file_name}' not found.")
        return None
    #
    except IOError as e:
    #
        print(f"Error: An I/O error occurred while writing to '{file_name}': {e}")
        return None
    #
    except Exception as e:
    #
        print(f"An unexpected error occurred: {e}") 
        return None
    #
    return True
#

def files_time_modified(filepath):
#
    """
        take_time when the file is modify
        args :
            filepath (string) : path of file
        return :
            file_mod_date (datetime) or None if error
        exemple :
            files_time_modified('test.txt')
            # return datetime.datetime(2021, 8, 10, 15, 30, 0, 0)
    """
    try :
    #
        timestamp = os.path.getmtime(filepath)
        file_mod_date = datetime.datetime.fromtimestamp(timestamp)
        return (file_mod_date)
    #
    except : # pylint: disable=bare-except
        return None
#



def check_update_file(filename, target_folder=None, mode_dev = False) :
#
    """
        The first call to this function is just to initialize a record. 
        The next calls will tell if the named file has had a change
        This function must be called once to instantiate its static variables.
        # [1] if the file has been modified # [0] if nothing happened # [None] if there was an error.
        args :
            filename (string) : name of file
            mode_dev (bool /optionnal) : True for see diagnostique
        exept :
            if file not found or file is clone in the folder
        ex :
        1/ check_update_file("main.py") (init)
        2/ check_update_file("main.py") (check)
        this function return (1): if main.py is modify
    """

    if mode_dev :
        print_blue('Fun : check_update_file()')
    path = find_file(filename, target_folder=target_folder, mode_dev=mode_dev)
    if not path :
    #
        if mode_dev :
            print_red("The path does not exist !")
        return None
    #
    else :
    #
        tmp_time = files_time_modified(path)
        if not tmp_time :
            return None
        rec_time = file.get_rec_time()
        new_time = file.get_new_time()
        if not rec_time :
        #
            if mode_dev :
            #
                print_yellow('First time call. Register file time...')
                print_blue('------------------------')
            #
            rec_time = file.change_rec_time(tmp_time)
            return 0
        #
        else :
        #
            new_time = file.change_new_time(tmp_time)
            if new_time != rec_time :
            #
                rec_time = file.change_rec_time(tmp_time)
                if mode_dev :
                #
                    print_green('The file has been modified')
                    print_blue('------------------------')
                #
                return 1
            #
            else :
            #
                if mode_dev :
                #
                    print_green('Result : The file has not been modified')
                    print_blue('------------------------')
                #
                return 0
            #
        #
    #
#

def create_search_folder(folder_name, mode_dev=False) :
#
    """
        Allows you to create a folder by specifying the path
        Args:
            folder_name (string): name of folder
            path_dir (string): The path where we will create the file
            mode_dev (bool, optional): True for see diagnostique
        Returns:
            string : the path of folder create or None if error
        exept :
            if file not found or folder is clone in the folder
        exemple :
            create_search_folder('test', 'PYTHON_')
            # create the folder test in the folder PYTHON_
    """
    if mode_dev is True :
        print_blue('Fun : create_search_folder')
    if folder_name is None :
    #
        if mode_dev is True :
            print_red('Error : folder_name is None')
            return None
    #
    folder_name = os.path.join(os.path.normpath(os.path.dirname(os.path.join(os.getcwd(), ''))) , folder_name)
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
        return True
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
        exept :
            if file not found or folder is clone in the folder
        exemple :
            create_search_file('test.txt', 'PYTHON_')
            # create the file test.txt in the folder PYTHON_
    """
    if mode_dev is True :
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
    path_dir = find_folder(path_dir, mode_dev=mode_dev)
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
        return True
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
        exept :
            if file not found or file is clone in the folder
        exemple :
            rm_file('test.txt', target_folder='PYTHON_')
            # delete the file test.txt in the folder PYTHON_
    """
    if mode_dev is True :
        print_blue('Fun : rm_dir')
    file_path = find_file(file, target_folder=target_folder, mode_dev=mode_dev)
    if file_path :
    #
        try:
        #
            os.remove(file_path)
            if mode_dev is True :
                print_green(f"The file '{file_path}' has been successfully deleted.")
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
        print_blue('Fun : rm_dir')
    folder_path = find_folder(folder, target_folder=target_folder, mode_dev=mode_dev)
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

def check_folder_is_clone(name, target_folder=None, mode_dev=False) :
#
    """
        Checks if the folder is in several copies from the program execution directory
        args :
            name (string) : name of folder
            target_folder (string /optional) : path of folder
            mode_dev (bool /optionnal) : True for see diagnostique
        return :
            True if folder is clone
    """
    if mode_dev is True :
        print_blue('Fun : check_folder_is_clone()')
    path = os.path.dirname(os.path.join(os.getcwd(), '../..'))
    name = os.path.basename(name)
    all_path = []
    count = 0
    for root, dir, files in os.walk(path) :
    #
        for elem in dir :
        #
            if name == elem:
            #
                if (target_folder is not None) :
                #   
                    if target_folder in os.path.normpath(os.path.join(root, elem)):
                    #   
                        all_path.append(os.path.join(root, elem))
                        count += 1
                   #   
                #   
                else :
                #   
                    all_path.append(os.path.join(root, name))
                    count += 1
                #   
            #
        #
    #
    if (len(all_path) > 1) :
    #
        if mode_dev is True :
            print_red(f'The folder as been cloned')
            print_red(f'Use var target_folder for make a choice in :\n{all_path}')
        return None
    #
    if (not all_path) :
    #
        if mode_dev is True :
            print_yellow('The folder not found !')
        return None
    #
    if mode_dev is True :
        print_green(f'The folder is unique :\n{os.path.normpath(all_path[0])}')
    return (os.path.normpath(all_path[0]))
#

def find_folder(name,  target_folder=None, mode_dev=False) :
#
    """
        Description :
            Search the folder path in the current directory
        Args:
            name (string): The name of the folder to search for
            mode_dev (bool, optional): True for see diagnostique
        Returns:
            (string): The folder path or None if there was an error
        Exept : 
            Limite of search in ".." or redirects the search to the current directory
        exemple :
            find_folder('PYTHON_', target_folder='PYTHON_')
            # search the path of folder PYTHON_ in the folder PYTHON_    
    """
    if mode_dev is True :
        print_blue('Fun : find_folder')
    if name is None :
    #
        print_red('Error : Var name is None')
        return None
    #
    if name == '.':
    #
        if mode_dev is True :
            print_yellow('Path redir : ' + os.path.normpath(os.path.dirname(os.path.join(os.getcwd(), ''))))
        return os.path.normpath(os.path.dirname(os.path.join(os.getcwd(), '')))
    #
    if name == '..':
    #
        if mode_dev is True :
            print_yellow('Path redir : ' + os.path.normpath(os.path.dirname(os.path.join(os.getcwd(), '..'))))        
        return os.path.normpath(os.path.dirname(os.path.join(os.getcwd(), '..')))
    #
    path = os.path.dirname(os.path.join(os.getcwd(), '.'))
    for root, dir, files in os.walk(path) :
    #
        for elem in dir :
        #        
            if name == elem:
            #
                if mode_dev is True :
                    print_yellow(f'Path directory is : {os.path.normpath(os.path.join(root, elem))}')
                if target_folder is not None :
                        return (check_folder_is_clone(name, target_folder=target_folder, mode_dev=mode_dev))
                else :
                        return (check_folder_is_clone(name, mode_dev=mode_dev))
            #
        #
    #
    if mode_dev is True :
        print_yellow('Path directory not found !')
    return (None)
#

def check_file_is_clone(name, target_folder=None, mode_dev=False) :
#
    """
        Checks if the file is in several copies from the program execution directory
        args :
            name (string) : name of file
            target_folder (string /optional) : path of folder
            mode_dev (bool /optionnal) : True for see diagnostique
        return :
            True if file is clone
        exemple :
            check_file_is_clone('main.py', target_folder='PYTHON_')
            # check if the file main.py is clone in the folder PYTHON_
    """
    if mode_dev is True :
        print_blue('Fun : check_file_is_clone()')
    path = os.path.dirname(os.path.join(os.getcwd(), ''))
    name = os.path.basename(name)
    if target_folder is not None :
    #
        path = find_folder(target_folder)
        if path == None :
            return None
    #
    count = 0
    all_path = []
    for root, dir, files in os.walk(path) :
    #
        for elem in files :
        #
            if name in elem:
            #
                all_path.append(os.path.join(root, name))
                count += 1
            #
        #
    #
    if count > 1 :
    #
        if mode_dev is True :
        #
            print_yellow(f'The file as been cloned :\n{all_path}')
            print_blue('<------------------------')
        #
        return True
    #
    if mode_dev is True :
        print_green('The file is unique')
    return False
#

def find_file(name, target_folder = None , mode_dev=False):
#
    """
        Search and take path with filename
        args :
            name (string) : name of file
            target_folder (string /optional) : path of folder
            mode_dev (bool /optionnal) : True for see diagnostique
        return :
            path (string) : path of file or None if error
        exept :
            if file not found or file is clone in the folder
        exemple :
            find_file('main.py', target_folder='PYTHON_')
            # search the path of file main.py in the folder PYTHON_
    """
    if mode_dev is True :
        print_blue('Fun : find_file()')
    if name is None :
    #
        if mode_dev is True :
            print_red('Var name is None')
        return None
    #
    name = os.path.basename(name)
    path = os.path.dirname(os.path.join(os.getcwd(), ''))
    if target_folder is not None :
    #
        path = find_folder(target_folder)
        if path == None :
        #
            print_red('Error : target_folder does not exist')
            return None
        #
        print_yellow('Mode target_folder activate :\n' + path)
    #
    if (check_file_is_clone(name, target_folder, mode_dev) is True) :
    #
        if mode_dev is True :
        #
            print_red('A potential error has been found. \n' +
                      'The search file exists in several copies.')
            print_blue('<------------------------')
        #
        return (None)
    #
    for root, dir, files in os.walk(path) :
    #
        for elem in files :
        # 
            if name in elem :
            #
                if mode_dev is True :
                #
                    print_green(f"Result path is :\n{os.path.join(root, name)}")
                    print_blue('----------------')
                #
                return os.path.join(root, name)
            #
        #
    #
    if mode_dev is True :
    #
        print_red('The path was not found')
        print_blue('----------------')
    #
    return None
#

def ls_files(path, target_folder=None, mode_dev=False) :
#
    """
        # Attempt to list the files in the folder
        args :
            path (string) : path of folder
            target_folder (string /optional) : path of folder
            mode_dev (bool /optionnal) : True for see diagnostique
        return :
            files_and_folders (list) or None if error
        exept :
            if file not found or folder is clone in the folder
        exemple :
            ls_files('utils', target_folder='PYTHON_', mode_dev=True)
            # list the files[] in PYTHON_/utils
    """
    if mode_dev is True :
        print_blue('Fun : ls_files()')
    path = find_folder(path, target_folder=target_folder, mode_dev=mode_dev)
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
        exept :
            if file not found or folder is clone in the folder
        exemple :
            is_folder_empty('test.txt', target_folder='PYTHON_', mode_dev=True)
            # return false
            # check if the file test.txt in the folder PYTHON_ is empty 
    """
    if mode_dev is True :
        print_blue('Fun : is_folder_empty()')
    files_and_folders = ls_files(path, target_folder=target_folder, mode_dev=mode_dev)
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

def ls_allfolder(name, target_folder=None, mode_dev=False) :
#
    """
        list all folder with path absolute
        args :
            name (string) : name of folder for search
            target_folder (string /optional) : path of folder
            mode_dev (bool /optionnal) : True for see diagnostique
        return :
            all_path (list) : list path of folder
        exemple :
            ls_allfolder('PYTHON_', target_folder='PYTHON_', mode_dev=True)
            # list all folder with name PYTHON_ in the folder PYTHON_
    """
    if mode_dev is True :
        print_blue('Fun : ls_allfolder()')
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
        print_blue('Fun : read_no_error')
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
        print_blue('Fun : readfile_to_str')
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
        print_blue('Fun : readfile_to_str')
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

def rm_filesdir(path, target_folder=None, mode_dev=False) :
#
    """
        # Attempt to remove all files in the folder
        args :
            path (string) : path of folder
            target_folder (string /optional) : path of folder
            mode_dev (bool /optionnal) : True for see diagnostique
        return :
            path (string) or None if error
            exemple : rm_filesdir('utils', target_folder='PYTHON_', mode_dev=True)
            # delete the files in PYTHON_/utils/*
    """
    if mode_dev is True :
        print_blue('Fun : rm_filesdir()')
    all_files = ls_files(path, target_folder=target_folder, mode_dev=mode_dev)
    if (all_files is None) :
        return None
    for file in all_files :
        file = find_file(file, target_folder=path, mode_dev=mode_dev)
        if (file is not None) :
            rm_file(file, target_folder=path, mode_dev=mode_dev)
    return path
#

def rm_force(path, target_folder=None, mode_dev=False) :
#
    """
        # Attempt to remove the file or the folder and all files in the folder
        args :
            path (string) : path of folder to delete
            target_folder (string /optional) : path of folder
            mode_dev (bool /optionnal) : True for see diagnostique
        return :
            path (string) or None if error
        exept :
            if file not found or file is clone in the folder
        exemple :
            rm_force('test1.txt', target_folder='PYTHON_', mode_dev=True)
            # delete the file test1.txt in the folder PYTHON_
    """
    if mode_dev is True :
        print_blue('Fun : rm_force()')
    find_path_folder = os.path.join(os.path.normpath(os.path.dirname(os.path.join(os.getcwd(), ''))) , find_path_folder)
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
            all_folder = ls_allfolder(find_path_folder, target_folder=target_folder, mode_dev=mode_dev)
            all_folder.reverse()
            for elem in all_folder :
            # 
                rm_filesdir(elem, target_folder=path, mode_dev=mode_dev)
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
            content = "Hello world"
            write_in_file('path/test1.txt', 'content', target_folder='PYTHON_', mode_dev=True)
    """
    if mode_dev is True :
        print_blue('Fun : write_in_file')
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

def is_valid_path(path) :
#
    """Check if the path exists on the current system"""
    return (os.path.exists(path))
#

def path_default(path = None, mode_dev = False) :
#
    """
    Allows you to choose or not a default path. fun :
    If no path specified, it will be the path of the current project repo,
    otherwise it will be the one given in parameter
    """
    if mode_dev :
        print_blue('Fun : path_default')
    if not path :
        path = os.getcwd()
    if not path.endswith(os.path.sep):
        path += os.path.sep
    if is_valid_path(path) :
        if mode_dev :
            print_green(f'The path by default is : {path}' )
            print_blue('---------------')
        return path
    else :
        if mode_dev :
            print_green('The path by default is false...')
            print_blue('---------------')
        return None
#

def is_dir(path, mode_dev = False) :
#
    """Determines if the path points to a folder"""
    if mode_dev is True :
        print_blue('Fun : is_dir()')
    if Path(path).is_dir() is True :
    #
        if mode_dev is True :
            print_yellow(f'Path : {path}  | is dir [True]')
        return (True)
    #
    else :
    #
        if mode_dev is True :
            print_yellow(f'Path : {path}  | is not a dir [False]')
        return (False)
    #
#

def is_file_search(path, mode_dev = False) :
#
    """Determines if the path points to a file"""
    if mode_dev is True :
        print_blue('Fun : is_file()')
    path = find_file(path, mode_dev)
    if path is None :
    #
        if mode_dev is True :
            print_red('Path error, setting -> [None]...')
        return None
    #
    if Path(path).is_file() is True :
    #
        if mode_dev is True :
            print_yellow(f'Path : {path}  | is file [True]')
        return True
    #
    else :
    #
        if mode_dev is True :
            print_yellow(f'Path : {path}  | is not a file [False]')
        return False
    #
#

def check_operating_system(mod_dev = False) :
#
    """ 
    Return name of operating system
    opt(mod_dev = True) for see diagnostic
    """
    if mod_dev is True :
        print_blue('Fun : check_operating_system()')
    #-------------------------------
    if os.name == 'posix' :
        if mod_dev is True :
            print_green('Result : Linux or MacOs')
    elif os.name == 'nt':
        if mod_dev is True :
            print_green('Result : Windows')
    elif os.name == 'java' :
        if mod_dev is True :
            print_green('Result : Jython environment')
    else:
        if mod_dev is True :
            print_green(f"Rsult : Unrecognized platform: {os.name}")
    if mod_dev :
        print_blue('----------------')
    return os.name
#