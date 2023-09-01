import os
from utils.print.print_color import print_blue, print_green, print_red, print_yellow

def find_directory(name, mode_dev=False) :
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
                return (os.path.normpath(os.path.join(root, elem)))
            #
        #
    #
    if mode_dev is True :
        print_yellow('Path directory not found !')
    return (None)
#
