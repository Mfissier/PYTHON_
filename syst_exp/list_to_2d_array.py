from utils.print.print_color import print_blue, print_green, print_red, print_yellow

def list_to_2d_array(input_list, mode_dev=False):
    """
        This function converts a list to a 2D array.
        @param list( ['',] ) input_list: The list to convert
        @return tab( [[],] ): The 2D array
    """
    if mode_dev:
        print_blue("Fun : list_to_2d_array")
    if input_list is None:
    #  
        if mode_dev:
            print_red("The list is None.")
        return None
    #
    array_2d = []
    for idx, map_with_enemy in enumerate(input_list, start=1):
    #
        if idx <= len(input_list):
            array_2d.append(map_with_enemy)
    #
    if mode_dev:
        print_yellow("The list is converted to a 2D array.")
    return array_2d