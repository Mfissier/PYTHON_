from syst_exp.calculate_player_to_enemy_moves import check_characters_map_is_good, check_map_is_rect, reconstruct_map2D
from utils.files.pyos import create_json_file, create_search_file, create_search_folder, find_file, readfile_to_json
from utils.print.print_color import print_red

def fill_map2D_origin(map2D_origin, mode_dev=False) :
#
    """
        This function fills the map2D_origin.json file.
        The map is represented as a list of strings, where:
        @param ( ['',] ) map2D: The 2D map
        - '0' represents a free cell
        - '1' represents a wall
        - 'P' represents the player
        - 'E' represents the enemy
        @return ( bool ): True if the map has a bad characters, False otherwise
    """
    if map2D_origin is None:
    #
        if mode_dev :
            print_red("The map is None.")
        return False
    #
    if (check_map_is_rect(map2D_origin, mode_dev=mode_dev) == False) :
        map2D_origin = reconstruct_map2D(map2D_origin, mode_dev=mode_dev)
    if (check_characters_map_is_good(map2D_origin, mode_dev=mode_dev) == False) :
    #
        if mode_dev :
            print_red("The map has a bad characters.")
        return False
    #
    import json
    BOT_IA = readfile_to_json('data/IA/IA.json', mode_dev=mode_dev)
    if BOT_IA is None :
    #
        if mode_dev :
            print_red("The file [IA.json] error : read file or open file.")
        return False
    #
    BOT_IA = json.loads(BOT_IA)
    BOT_IA["Map"] = map2D_origin
    if (create_json_file(BOT_IA, find_file('IA.json'), mode_dev=mode_dev) == None) :
        return False
    return True
#