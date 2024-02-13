#!/usr/bin/env python
# -*- codage : utf-8 -*-
"""
    Main fun
"""
from syst_exp.create_maps_with_diff_ennemies import create_maps_with_different_enemies
from syst_exp.calculate_distance2D import calculate_distance2D
from syst_exp.fill_all_map2D_diff_ennemies import fill_all_map2D_diff_ennemies
from syst_exp.fill_map2D_origin import fill_map2D_origin
from syst_exp.list_to_2d_array import list_to_2d_array
from utils.files.pyos import *
from syst_exp.calculate_player_to_enemy_moves import calculate_player_to_enemy_moves
import json

def main() :
#
    """
    This main is juste for test
    """
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
    map_2d = [
        ["E","0","0","0","0","0","0","0","1"],
        ["0","0","E","0","0","0","1","0","0"],
        ["0","1","1","1","1","1","1","1","0"],
        ["0","0","0","0","0","0","1","0","P"]
    ]
    import json

    if fill_map2D_origin(map_2d, mode_dev=True) == False:
        print_red("The map is None.")
        return False

    if fill_all_map2D_diff_ennemies(map_2d, mode_dev=True) == False:
        print_red("The calcul failed !")
        return False

    data_map = readfile_to_json('data/map2D/map2D_diff_ennemies.json', mode_dev=True)
    data_map = json.loads(data_map)  # Parse the JSON string into a dictionary
    print(data_map)

#
if __name__ == "__main__":
    main()