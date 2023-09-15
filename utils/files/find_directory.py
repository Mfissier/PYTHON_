import os
from utils.print.print_color import print_blue, print_green, print_red, print_yellow


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

def find_directory(name,  target_folder=None, mode_dev=False) :
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
            find_directory('PYTHON_', target_folder='PYTHON_')
            # search the path of folder PYTHON_ in the folder PYTHON_    
    """
    if mode_dev is True :
        print_blue('fun : find_directory')
    if name is None :
    #
        print_red('Error : Var name is None')
        return None
    #
    name = os.path.normpath(name)
    if name == '.':
    #
        if mode_dev is True :
            print_yellow('Path redir : ' + os.path.normpath(os.path.dirname(os.path.join(os.getcwd(), ''))))
        return os.path.normpath(os.path.dirname(os.path.join(os.getcwd(), '')))
    #
    if name == '..':
    #
        if mode_dev is True :
            print_yellow('Path redir : ' + os.path.normpath(os.path.dirname(os.path.join(os.getcwd(), '../..'))))        
        return os.path.normpath(os.path.dirname(os.path.join(os.getcwd(), '../..')))
    #
    path = os.path.dirname(os.path.join(os.getcwd(), '../'))
    name = os.path.basename(name)
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
