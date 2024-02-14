
from syst_exp.calculate_player_to_enemy_moves import calculate_player_to_enemy_moves
from syst_exp.create_maps_with_diff_ennemies import create_maps_with_different_enemies
from syst_exp.handler_data.init_data import formulaire_ennemy
from syst_exp.list_to_2d_array import list_to_2d_array
from utils.files.pyos import create_json_file, create_search_folder, readfile_to_json
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
    if (create_search_folder('data', mode_dev=mode_dev) is None) :
    #
        if mode_dev :
            print_red("The folder [data] error : create")
        return False
    #
    BOT_IA = readfile_to_json('data/IA/IA.json', mode_dev=mode_dev)
    if BOT_IA is None :
    #
        if mode_dev :
            print_red("The file [IA.json] error : read file or open file.")
        return False
    #
    BOT_IA = json.loads(BOT_IA)
    if "Ennemy" not in BOT_IA :
    #
        if mode_dev :
            print_red("The file [IA.json] error : the key [Ennemy] not found.")
        return False
    #
    i = 0
    for map in map_2d:
        result = calculate_player_to_enemy_moves(map, mode_dev=mode_dev)
        if result is False:
            if mode_dev:
                print_red("The map is None.")
            return False
        if result:
            if i > 0:
                BOT_IA["Ennemy"].append(formulaire_ennemy())
            BOT_IA["Ennemy"][i]["distance"] = int(result[0])
            BOT_IA["Ennemy"][i]["path"].append(result[1])
            BOT_IA["Ennemy"][i]["position"] = result[1][-1]
            i += 1
    #
    if (create_json_file(BOT_IA, 'data/IA/IA.json', mode_dev=mode_dev) == None) :
    #
        if mode_dev :
            print_red("The map is None.")
        return False
    #
    if mode_dev :
        print_yellow("The list of maps with different enemies is created.")
    return True
#