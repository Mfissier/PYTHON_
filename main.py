#!/usr/bin/env python
# -*- codage : utf-8 -*-
"""
    Main fun
"""
from syst_exp.create_maps_with_diff_ennemies import create_maps_with_different_enemies
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
    map_2d = [
        "E00000000",
        "000000100",
        "011111110",
        "000E0000P"
    ]
    fill_map2D_origin(map_2d, mode_dev=True)
    fill_all_map2D_diff_ennemies(map_2d, mode_dev=True)
    # test = readfile_to_json('data/map2D/map2D_diff_ennemies.json', mode_dev=True)
    # test = 
    # result = json.loads(test)
    # print(result["map2D_diff_ennemies"])
    # map_2d = create_maps_with_different_enemies(map_2d, mode_dev=True)
    # list_tab = []
    # for map in map_2d:
    # #
    #     list_tab.append(list(map))
    #     new_tab = list_to_2d_array(map, mode_dev=True)
    # #
        # test = calculate_player_to_enemy_moves(new_tab, mode_dev=True)
#
if __name__ == "__main__":
    main()