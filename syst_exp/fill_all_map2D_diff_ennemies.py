
from syst_exp.calculate_player_to_enemy_moves import calculate_player_to_enemy_moves
from syst_exp.create_maps_with_diff_ennemies import create_maps_with_different_enemies
from syst_exp.list_to_2d_array import list_to_2d_array
from utils.files.pyos import create_json_file, create_search_folder
import json

from utils.print.print_color import print_red, print_yellow

def fill_all_map2D_diff_ennemies(map2D_origin, mode_dev=False) :
#
    map_2d = create_maps_with_different_enemies(map2D_origin, mode_dev=mode_dev)
    if (map_2d is None) :
    #
        if mode_dev :
            print_red("The map is None.")
        return False
    #
    create_search_folder('data', mode_dev=mode_dev)
    create_search_folder('data/map2D', mode_dev=mode_dev)
    map_stat = {
        "map_nb_path" : [],
        "map_path_mv" : []
    }
    for map in map_2d:
    #
        result = calculate_player_to_enemy_moves(map, mode_dev=mode_dev)
        if result is False  :
        #
            if mode_dev :
                print_red("The map is None.")
            return False
        #
        map_stat["map_nb_path"].append(result[0])
        map_stat["map_path_mv"].append(result[1]) 
    #
    data = {
        "map2D_diff_ennemies": map_2d,
        "map_stat": map_stat
    }
    if (create_json_file(data, 'data/map2D/map2D_diff_ennemies.json', mode_dev=mode_dev) == None) :
    #

        if mode_dev :
            print_red("The map is None.")    
        return False
    #
    if mode_dev :
        print_yellow("The list of maps with different enemies is created.")
    return True
#