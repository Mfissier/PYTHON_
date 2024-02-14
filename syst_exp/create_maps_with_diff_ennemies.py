
from utils.print.print_color import print_blue, print_green, print_red, print_yellow


def create_maps_with_different_enemies(original_map, mode_dev=False):
    
    """
        This function creates a list of maps with different enemies.
        The map is represented as a list of strings, where:
        - '0' represents a free cell
        - '1' represents a wall
        - 'P' represents the player
        - 'E' represents the enemy
        @param ( ['',] ) original_map: The original map
        @return ( [ ['',], ] ): The list of maps with different enemies
    """
    if mode_dev:
        print_blue("Fun : create_maps_with_different_enemies")
    if original_map is None:
    #  
        if mode_dev:
            print_red("The map is None.")
        return None
    #  
    maps_with_enemies = []
    # Find the positions of the 'E' enemies in the original map
    enemy_positions = []
    for i, row in enumerate(original_map):
    #    
        for j, char in enumerate(row):
        #    
            if char == 'E':
                enemy_positions.append((i, j))
        #    
    #    
    # For each enemy position, create a copy of the original map and modify it
    for idx, enemy_pos in enumerate(enemy_positions):
    #    
        # Create a copy of the original map
        new_map = [list(row) for row in original_map]
        # Modify the copy of the map to place the current enemy at '0'
        for index, enemy_position in enumerate(enemy_positions):
            if (idx != index):
                new_map[enemy_position[0]][enemy_position[1]] = '0'
        # Add the modified map to the list
        maps_with_enemies.append(new_map)
    #
    if mode_dev:
        print_yellow("The list of maps with different enemies is created.")
    return maps_with_enemies