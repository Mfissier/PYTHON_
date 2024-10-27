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
from create_data.create_data_set import *
def main() :
#
    """
    This main is juste for test
    """

    # output_path = normalize_json("all_samples_train1.json", mod_dev = True)
    tokenized_data = tokenize_json_file("all_samples_train1_normalize.json", "openai-community/gpt2", mod_dev=True)

#

if __name__ == "__main__":
    main()