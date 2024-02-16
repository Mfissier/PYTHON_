
from utils.files.pyos import create_json_file
from utils.print.print_color import print_blue, print_red, print_yellow


def player_pos (BOT_IA, mode_dev = False) :
    """
    This fun is for get the player position
    return : list or False if the player position is not found
    BOT_IA : dict
    mode_dev : boolean (default False)
    example :
    player_pos(BOT_IA, mode_dev=True)
    """
    if mode_dev :
        print_blue("Fun :player_pos :")
    if BOT_IA is None :
    #
        if mode_dev :
            print_red("The file [IA.json] error : the file is None.")
        return False
    #
    import json
    BOT_IA = json.loads(BOT_IA)
    if "Map" not in BOT_IA :
    #
        if mode_dev :
            print_red("The file [IA.json] error : the key [Map] not found.")
        return False
    #
    map = BOT_IA["Map"]
    if "Player" not in BOT_IA :
    #
        if mode_dev :
            print_red("The file [IA.json] error : the key [Player] not found.")
        return False
    #
        
    for i in range(len(map)) :
    #
        for j in range(len(map[i])) :
        #
            
            if map[i][j] == "P" :
            #
                print_yellow(BOT_IA["Player"]["position"])
                
                BOT_IA["Player"]["position"] = [i,j]
                print(i,j)
                if mode_dev :
                    print_blue("The player position is : " + str(BOT_IA["Player"]["position"]))
                if (create_json_file(BOT_IA, 'data/IA/IA.json', mode_dev=mode_dev) == None) :
                #
                    if mode_dev :
                        print_red("The map is None.")
                    return False
                #
                return BOT_IA["Player"]["position"]
            #
        #
    #
    return False
