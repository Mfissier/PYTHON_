# from collections import deque
from utils.files.pyos import * 
import heapq

def check_map_is_rect(map2D, mode_dev=False) :
#
    """
        This function checks if the 2D map is valid.
        The map is represented as a list of strings, where:
        @param ( ['',] ) map2D: The 2D map
        - '0' represents a free cell
        - '1' represents a wall
        - 'P' represents the player
        - 'E' represents the enemy
        @return ( bool ): True if the map is rectangular, False otherwise
    """
    if mode_dev :
        print_blue("Fun : check_map_is_rect")
    if map2D is None:
    #
        if mode_dev :
            print_red("The map is None.")
        return False
    #
    for row in map2D:
    #
        if len(row) != len(map2D[0]):
        #
            if mode_dev :
                print_red("The map is not rectangular.")
            return False
        #
    #
    if mode_dev :
        print_yellow("The map is rectangular.")
    return True
#

def check_characters_map_is_good(map2D, mode_dev=False) :
#
    """
        This function checks if the 2D map is valid.
        The map is represented as a list of strings, where:
        @param ( ['',] ) map2D: The 2D map
        - '0' represents a free cell
        - '1' represents a wall
        - 'P' represents the player
        - 'E' represents the enemy
        - 'I' represents the invocation
        - 'A' represents the allie
        @return ( bool ): True if the map has a bad characters, False otherwise
    """
    if mode_dev :
        print_blue("Fun : check_characters_map_is_good")
    if map2D is None:
    #
        if mode_dev :
            print_red("The map is None.")
        return False
    #
    check_players = 0
    check_ennemy = 0
    for row in map2D:
    #
        for char in row:
        #
            # if char not in ['0', '1', 'P', 'E']:
            # #
            #     if mode_dev :
            #         print_red("The map contains invalid characters.")
            #     return False
            # #
            if char == 'P':
                check_players += 1
            elif char == 'E':
                check_ennemy += 1
        #
    # if player is dead and game continue ?
    if check_players != 1 or check_ennemy < 1:
    #
        if mode_dev :
            print_red("The map need one player and one ennemy")
        return False
    #
    if mode_dev :
        print_yellow("The map is valid.")
    return True
#

def reconstruct_map2D(map2D, mode_dev=False) :
#
    """
        This function reconstructs the maps if is not rectangular.
        The map is represented as a list of strings, where:
        @param ( ['',] ) map2D: The 2D map
        - '0' represents a free cell
        - '1' represents a wall
        - 'P' represents the player
        - 'E' represents the enemy
        - 'I' represents the invocation
        - 'A' represents the allie
        @return ( ['',] ): The new 2D map
    """
    if mode_dev :
        print_blue("Fun : reconstruct_map2D")
    len_max = 0
    for row in map2D:
    #
        if len(row) > len_max:
        #
            len_max = len(row)
        #
    #
    new_map2D = []
    for row in map2D:
    #
        new_row = row
        while len(new_row) < len_max:
            new_row += '0'
        new_map2D.append(new_row)
    #
    if mode_dev :
        print_green(f"The new map is : {new_map2D}")
    return new_map2D
#

def reconstruct_path(parents, start, goal, mode_dev=False):
#
    """
        This function reconstructs the path from the start to the goal.
        @param ( {} ) parents: The dictionary of parents
        @param ( tuple ) start: The start position
        @param ( tuple ) goal: The goal position
        @return ( [tuple,] ): The path from the start to the goal
    """
    if mode_dev :
        print_blue("Fun : reconstruct_path")
    path = []
    current = goal
    while current != start:
    #
        path.append(current)
        current = parents[current]
    #
    path.append(start)
    if mode_dev :
        print_green(f"The path is : {path}")
    return list(reversed(path))
#

def calculate_player_to_enemy_moves(map2D, mode_dev=False) :
#
    """
        This function calculates the distance between the player and the enemy in a 2D map.
        The map is represented as a list of strings, where:
        @param ( ['',] ) map2D: The 2D map
        - '0' represents a free cell
        - '1' represents a wall
        - 'P' represents the player
        - 'E' represents the enemy
        @return ( int ): The distance between the player and the enemy
        The distance is calculated using the A* algorithm.
        If no path is found, the function returns -1.
    """
    if mode_dev :
        print_blue("Fun : map2D_calcul_player_ennemy_mouve")
    # Check if the map is rectangular and reconstruct it if necessary
    if (check_map_is_rect(map2D, mode_dev=mode_dev) == False) :
        map2D = reconstruct_map2D(map2D, mode_dev=mode_dev)
    # Check if the map is valid
    if (check_characters_map_is_good(map2D, mode_dev=mode_dev) == False) :
        return False
    rows = len(map2D)
    cols = len(map2D[0])
    # Find the positions of the player (P) and the enemy (E)
    player_pos = None
    enemy_pos = None
    for i in range(rows):
    #
        for j in range(cols):
        #
            if map2D[i][j] == 'P':
                player_pos = (i, j)
            elif map2D[i][j] == 'E':
                enemy_pos = (i, j)
        #
    #
    # Check if the player and enemy have been found
    if player_pos is None or enemy_pos is None:
        return False  # Unable to calculate distance

    # Define possible movements (up, down, left, right)
    directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]
    distance = None
    path = None
    # Initialize the priority queue for A*
    priority_queue = []
    heapq.heappush(priority_queue, (0, player_pos))

    # Create a dictionary to keep track of visited cells and distances
    visited = {player_pos: 0}
    parents = {}
    while priority_queue:
    #
        distance, current_pos = heapq.heappop(priority_queue)
        # Check if the enemy has been reached
        if current_pos == enemy_pos:
        #
            if mode_dev :
                print_yellow(f"The distance between the player and the enemy is : {distance} cells.")
            path = reconstruct_path(parents, player_pos, enemy_pos, mode_dev=mode_dev)
            return distance, path
        #
        for dx, dy in directions:
        #
            new_x, new_y = current_pos[0] + dx, current_pos[1] + dy
            new_pos = (new_x, new_y)
            # Check if the new position is valid and not a wall
            if 0 <= new_x < rows and 0 <= new_y < cols and map2D[new_x][new_y] != '1':
            #
                new_distance = distance + 1
                # Check if the new position has not been visited or if a shorter path has been found
                if new_pos not in visited or new_distance < visited[new_pos]:
                #
                    heapq.heappush(priority_queue, (new_distance, new_pos))
                    visited[new_pos] = new_distance
                    parents[new_pos] = current_pos
                #
            #
        #
    #
    if mode_dev :
        print_red("No path was found.")
    return distance, path
#