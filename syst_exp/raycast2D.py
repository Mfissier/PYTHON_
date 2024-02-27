import math
from syst_exp.get_visible_tiles import get_visible_tiles
from utils.files.pyos import create_json_file

from utils.print.print_color import print_blue, print_red, print_yellow

def norm_grid(grid) :
#
    for i in range(len(grid)) :
    #
        for j in range(len(grid[i])) :
        #
            if grid[i][j] == "E" :
                grid[i][j] = "1"
            elif grid[i][j] == "A" :
                grid[i][j] = "1"
            elif grid[i][j] == "I" :
                grid[i][j] = "1"
            elif grid[i][j] == "IA" :
                grid[i][j] = "1"
            elif grid[i][j] == "IE" :
                grid[i][j] = "1"
            elif grid[i][j] == "IP" :
                grid[i][j] = "1"
    return grid
#
    

def raycast_save2D(BOT_IA, grid, player_position, mode_dev=False) :
#
    """
    This function is used to save the visible cells in the json file.
    @BOT_IA : dict, the bot IA
    @grid : list of lists, representing the tile-based map where 0 means free space and 1 means wall
    @player_position : tuple, (x, y) coordinates of the player's position
    @mode_dev : boolean, if True, the function will display the debug mode
    """

    swap = lambda x, y: (y, x)
    player_position = swap(*player_position)
    grid = norm_grid(grid)
    visible_cells = get_visible_tiles(grid, player_position, 20)
    for tile_pos in visible_cells:
        x, y = tile_pos
        if grid[y][x] == "0":
            grid[y][x] = "V"
    for line in grid:
        print(line)
    if visible_cells is None:
    #
        if mode_dev:
            print_red("The visible_cells is None.")
        return False
    #
    BOT_IA["Visibility"] = grid
    if (create_json_file(BOT_IA, 'data/IA/IA.json', mode_dev=mode_dev) == None) :
    #
        if mode_dev :
            print_red("The map is None.")
        return False
    #
    print_yellow(BOT_IA)
#