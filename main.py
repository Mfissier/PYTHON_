#!/usr/bin/env python
# -*- codage : utf-8 -*-
"""
    Main fun
"""

from utils.files.pyos import *
from syst_exp.calculate_player_to_enemy_moves import calculate_player_to_enemy_moves  

def main() :
#
    """
    This main is juste for test
    """
    find_folder('test', target_folder='PYTHON_', mode_dev=True)
    map_2d = [
        "000",
        "00000000E",
        "011111111",
        "00000"
    ]

    distance = calculate_player_to_enemy_moves(map_2d, mode_dev=True)
#

if __name__ == "__main__":
    main()
