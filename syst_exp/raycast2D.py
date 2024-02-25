import math
from utils.files.pyos import create_json_file

from utils.print.print_color import print_blue, print_red, print_yellow

def raycast2D(grid, player_position, mode_dev=False):
#
    '''
    Raycast2D function
    @param grid: list
    @param player_position: tuple
    @return visible_cells: list
    exemple:
    grid = [
        [0, 0, 0, 0, 0],
        [0, "P", 0, 0, 0],
        [0, 1, 1, 1, 0],
        [0, 0, 0, 0, 0]
    ]
    player_position = (1, 1)
    visible_cells = raycast2D(grid, player_position)
    '''
    if mode_dev:
        print_blue("fun : raycast2D.")
    if (grid is None) or (player_position is None):
    #
        if mode_dev:
            print_red("The grid or the player position is None.")
        return None
    #
    rows = len(grid)
    cols = len(grid[0])
    visible_cells = [[' ' for _ in range(cols)] for _ in range(rows)]
    visible_cells[player_position[0]][player_position[1]] = 'P'
    for visible_cell in visible_cells:
    #
        for cell in visible_cell:
        #
            if cell == 'I':
                cell = '1'
            if cell == 'E':
                cell = '1'
            if cell == 'IE':
                cell = '1'
            if cell == 'A' :
                cell = '1'
            if cell == 'IA' :
                cell = '1'
            if cell == 'IP' :
                cell = '1'
        #
    #
    for angle in range(360):
    #
        angle_radians = math.radians(angle)
        x = player_position[1] + 0.5
        y = player_position[0] + 0.5
        step_x = math.cos(angle_radians)
        step_y = math.sin(angle_radians)
        while True:
        #
            x += step_x
            y += step_y
            if not (0 <= y < rows and 0 <= x < cols):
                break
            if grid[int(y)][int(x)] == "1":
            #
                visible_cells[int(y)][int(x)] = '1'
                break
            #
            visible_cells[int(y)][int(x)] = 'V'
        #
    #
    if mode_dev :
    #
        for row in visible_cells:
            print_yellow(row)
    #
    return visible_cells
#

def raycast_save2D(BOT_IA, grid, player_position, mode_dev=False) :
#
    """
    """
    visible_cells = raycast2D(grid, player_position, mode_dev)
    if visible_cells is None:
    #
        if mode_dev:
            print_red("The visible_cells is None.")
        return False
    #
    BOT_IA["Visibility"] = visible_cells
    if (create_json_file(BOT_IA, 'data/IA/IA.json', mode_dev=mode_dev) == None) :
    #
        if mode_dev :
            print_red("The map is None.")
        return False
    #
    print_yellow(BOT_IA)
#