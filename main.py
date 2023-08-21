#!/usr/bin/env python
# -*- codage : utf-8 -*-
"""
    Main fun
"""
from utils.files.find_file import find_file
from utils.syst_os.take_plateform import check_operating_system

def main() :
#
    """
    This main is juste for test
    """
    check_operating_system(mod_dev = True)
    find_file("main.py", mod_dev = True)
#

if __name__ == "__main__":
    main()
