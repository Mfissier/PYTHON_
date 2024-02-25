from utils.files.pyos import *

def formulaire_ennemy() :
#
    """
        This function returns the formulaire of the ennemy.
        @return ( dict ) : The formulaire of the ennemy
    """
    return {
        "position" : [0,0],
        "distance_pm" : 0,
        "distance_door" : 0,
        "path" : [],
        "life" : 0,
        "Spell" : [""]
    }
#

def init_data(mode_dev=False) :
#
    """
        This function initializes the data of IA.
        @return ( bool ): True if the data is initialized, False otherwise
    """
    if mode_dev :
        print_blue("Fun : init_data")
    BOT_IA = {
        "Map" : ["P","E", "I", "A", "1", "0"],
        "Ennemy" : [
            {
                "position" : [0,0],
                "distance_door" : 0,
                "distance_pm" : 0,
                "path" : [],
                "life" : 0,
                "Spell" : [""]
            }
        ],
        "Player" :
        {
            "position" : [0,0],
            "action" : [""],
            "life" : 0,
            "Visibility" : [""],
            "Spell" : [""]
        },
        "Invocation" : [
            {
                "position" : [0,0],
                "distance_pm" : 0,
                "distance_door" : [0,0],
                "action" : [""],
                "life" : 0,
                "Spell" : [""]
            }
        ],
        "Allie" : [
            {
                "position" : [0,0],
                "distance_pm" : 0,
                "distance_door" : [0,0],
                "action" : [""],
                "life" : 0,
                "Spell" : [""]
            }
        ]
    }
    
    if (create_search_folder('data', mode_dev=mode_dev) == None) :
    #
        if mode_dev :
            print_red("The folder [data] error : create")
        return False
    #
    if (create_search_folder('data/IA', mode_dev=mode_dev) == None) :
    #
        if mode_dev :
            print_red("The folder [data/IA] error : create")
        return False
    #
    if (create_search_file('IA.json', 'IA', mode_dev=mode_dev) == None) :
    #
        if mode_dev :
            print_red("The files [data/IA/IA.json] error : create")
        return False
    #
    if (create_json_file(BOT_IA, find_file('IA.json', mode_dev=mode_dev), mode_dev=mode_dev) == None) :
    #
        if mode_dev :
            print_red("The files [data/IA/IA.json] error : write json file")
        return False
    #
    if mode_dev :
        print_yellow("The data is initialized.\n----------------------\n")
    return (BOT_IA)
#