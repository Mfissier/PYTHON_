import math

def raycast(grid, player_position):
    rows = len(grid)
    cols = len(grid[0])
    visible_cells = [[cell for cell in row] for row in grid]

    # Nombre de rayons et angle de vision du joueur
    num_rays = 500
    fov = 360  # Angle de vision en degrés
    ray_angle_increment = fov / num_rays  # Incrément d'angle pour chaque rayon

#================================================================================================
    # Paramètres de visibilité basés sur la distance et l'angle
    max_visibility_angle = 45 # Angle maximal pour la visibilité
#================================================================================================
    for ray_number in range(num_rays):
        # Calculer l'angle du rayon en radians
        ray_angle = math.radians(player_position[1] - fov / 2 + ray_number * ray_angle_increment)

        # Initialiser les coordonnées du rayon au joueur
        ray_x, ray_y = player_position

        # Déterminer la direction du rayon
        ray_dx = math.cos(ray_angle)
        ray_dy = math.sin(ray_angle)

        # Itérer le long du rayon jusqu'à ce qu'il touche un mur ou sorte de la grille
        while 0 <= int(ray_x) < rows and 0 <= int(ray_y) < cols and grid[int(ray_x)][int(ray_y)] != 1:
            visible_cells[int(ray_x)][int(ray_y)] = 'V'
            ray_x += ray_dx
            ray_y += ray_dy

        # Marquer les cases derrière le mur avec 'X'
        while 0 <= int(ray_x) < rows and 0 <= int(ray_y) < cols:
            angle_difference = abs(math.degrees(math.atan2(ray_y - player_position[1], ray_x - player_position[0]) - player_position[1]))
            if angle_difference <= max_visibility_angle:
                if visible_cells[int(ray_x)][int(ray_y)] != 'P' and visible_cells[int(ray_x)][int(ray_y)] != 1:
                    visible_cells[int(ray_x)][int(ray_y)] = 'X'
            else:
                if visible_cells[int(ray_x)][int(ray_y)] != 'P' and visible_cells[int(ray_x)][int(ray_y)] != 1:
                    print(angle_difference)
                    visible_cells[int(ray_x)][int(ray_y)] = 'V'
            ray_x += ray_dx
            ray_y += ray_dy
  




    # Placer le joueur sur la grille visible
    visible_cells[player_position[0]][player_position[1]] = 'P'

    return visible_cells

# Exemple d'utilisation
grid = [
    [0, 0, 0,  0,  0, 0, 0, 0, 0],
    [0, 0, 0,  0,  0, 0, 0, 0, 0],
    [0, 1, 1,  1,  0, 0, 0, 0, 0],
    [0, 0, 0, 'P', 0, 0, 0, 0, 0],

]

player_position = (3, 3)
visible_cells = raycast(grid, player_position)


# Afficher le résultat
for row in visible_cells:
    print(row)

