def get_visible_tiles(grid, player_pos, sight_radius):
    """
    Get the visible tiles for the player within a given sight radius.

    Arguments:
    - grid : list of lists, representing the tile-based map where 0 means free space and 1 means wall
    - player_pos : tuple, (x, y) coordinates of the player's position
    - sight_radius : integer, the sight radius of the player

    Returns:
    - list of tuples representing the visible tiles for the player
    """
    visible_tiles = []

    for dy in range(-sight_radius, sight_radius + 1):
        for dx in range(-sight_radius, sight_radius + 1):
            x = player_pos[0] + dx
            y = player_pos[1] + dy

            if 0 <= x < len(grid[0]) and 0 <= y < len(grid):
                if (dx ** 2 + dy ** 2) <= sight_radius ** 2:
                    if not is_line_blocked(grid, player_pos, (x, y)):
                        visible_tiles.append((x, y))
    return visible_tiles

def is_line_blocked(grid, start_pos, end_pos):
    """
    Check if there's an obstructed line between two points on a given tile map.

    Arguments:
    - grid : list of lists, representing the tile-based map where 0 means free space and 1 means wall
    - start_pos : tuple, (x, y) coordinates of the starting point
    - end_pos : tuple, (x, y) coordinates of the ending point

    Returns:
    - True if the line between start_pos and end_pos is obstructed by a wall, False otherwise
    """

    x0, y0 = start_pos
    x1, y1 = end_pos

    dx = abs(x1 - x0)
    dy = abs(y1 - y0)
    sx = 1 if x0 < x1 else -1
    sy = 1 if y0 < y1 else -1
    err = dx - dy

    while True:
        if (x0, y0) == end_pos or (x0 < 0) or (y0 < 0) or (x0 >= len(grid[0])) or (y0 >= len(grid)):
            break
        if grid[y0][x0] == "1":
            return True
        e2 = 2 * err
        if e2 > -dy:
            err -= dy
            x0 += sx
        if e2 < dx:
            err += dx
            y0 += sy
    return False

