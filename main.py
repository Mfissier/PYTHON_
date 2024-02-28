#!/usr/bin/env python
# -*- codage : utf-8 -*-
"""
    Main fun
"""
from syst_exp.create_maps_with_diff_ennemies import create_maps_with_different_enemies
from syst_exp.calculate_distance2D import calculate_distance2D
from syst_exp.door_distance import door_distance
from syst_exp.fill_all_map2D_diff_ennemies import fill_all_map2D_diff_ennemies
from syst_exp.fill_map2D_origin import fill_map2D_origin
from syst_exp.handler_data.player_pos import player_pos
from syst_exp.list_to_2d_array import list_to_2d_array
from syst_exp.raycast2D import get_visible_tiles2D
from utils.files.pyos import *
from syst_exp.calculate_player_to_enemy_moves import calculate_player_to_enemy_moves
import json
from syst_exp.handler_data.init_data import init_data

def main() :
#
    """
    This main is juste for test
    """
    map_2d = [
        ["0","0","0","0","0","0","0","0","1"],
        ["0","0","E","0","0","0","0","0","0"],
        ["0","0","1","0","0","0","1","1","0"],
        ["0","0","P","0","0","0","1","0","0"]
    ]
    import json
    BOT_IA = init_data()
    if (fill_map2D_origin(map_2d) == False) :
    #
        print_red("The map is None.")
        return False
    #
    BOT_IA = readfile_to_json('data/IA/IA.json')
    playerpos = player_pos(BOT_IA, mode_dev=True)
    if (fill_all_map2D_diff_ennemies(map_2d, playerpos) == False) :
    #
        print_red("The calcul failed !")
        return False
    #
    BOT_IA = json.loads(BOT_IA)
    get_visible_tiles2D(BOT_IA,  map_2d, playerpos, mode_dev=True)
#

if __name__ == "__main__":
    main()