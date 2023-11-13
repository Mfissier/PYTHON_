#!/usr/bin/env python
# -*- codage : utf-8 -*-
"""
    Main fun
"""
from syst_exp.create_maps_with_diff_ennemies import create_maps_with_different_enemies
from syst_exp.list_to_2d_array import list_to_2d_array
from utils.files.pyos import *
from syst_exp.calculate_player_to_enemy_moves import calculate_player_to_enemy_moves

def main() :
#
    """
    This main is juste for test
    """
    find_folder('test', target_folder='PYTHON_', mode_dev=True)
    map_2d = [
        "E00000000",
        "00E000100",
        "01111111E",
        "00000000P"
    ]
    map_2d = create_maps_with_different_enemies(map_2d, mode_dev=True)
    for map in map_2d:
    #
        new_tab = list_to_2d_array(map, mode_dev=True)
        test = calculate_player_to_enemy_moves(new_tab, mode_dev=True)
    #
#
if __name__ == "__main__":
    main()