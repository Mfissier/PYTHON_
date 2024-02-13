from utils.files.pyos import *

def init_data(mode_dev=False) :
#
    """
        This function initializes the data of IA.
        @return ( bool ): True if the data is initialized, False otherwise
    """
    if mode_dev :
        print_blue("fun : init_data")
        BOT_IA = {
        "Map" : ["P","E", "I", "A", "1", "0"],
        "Ennemy" : [
            {
                "position" : [0,0],
                "distance" : 0,
                "path" : [[0,0],[0,0]],
                "life" : 0,
                "Spell" : [""]
            }
        ],
        "Player" :
        {
            "position" : [0,0],
            "distance" : 0,
            "action" : [""],
            "life" : 0,
            "Spell" : [""]
        },
        "Invocation" : [
            {
                "position" : [0,0],
                "distance" : 0,
                "action" : [""],
                "life" : 0,
                "Spell" : [""]
            }
        ],
        "Allie" : [
            {
                "position" : [0,0],
                "distance" : 0,
                "action" : [""],
                "life" : 0,
                "Spell" : [""]
            }
        ]
    }
    
    if (create_search_folder('data') == None) :
    #
        if mode_dev :
            print_red("The folder [data] error : create")
        return False
    #
    if (create_search_folder('data/IA') == None) :
    #
        if mode_dev :
            print_red("The folder [data/IA] error : create")
        return False
    #
    if (create_search_file('IA.json', 'IA') == None) :
    #
        if mode_dev :
            print_red("The files [data/IA/IA.json] error : create")
        return False
    #
    if (create_json_file(BOT_IA, find_file('IA.json')) == None) :
    #
        if mode_dev :
            print_red("The files [data/IA/IA.json] error : write json file")
        return False
    #
    if mode_dev :
        print_yellow("The data is initialized.\n----------------------\n")
    return (BOT_IA)
#