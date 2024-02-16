from utils.print.print_color import print_blue, print_red


def door_distance(position1, position2, mode_dev=False):
#
    """
    This function calculates the distance between two positions.
    @param ( list ) position1: The first position
    @param ( list ) position2: The second position
    @param ( bool ) mode_dev: The development mode
    @return ( int ) : The distance between the two positions
    """
    if mode_dev:
        print_blue("Fun : door_distance :")
    if position1 is None or position2 is None:
    #
        if mode_dev:
            print_red("The position is None.")
        return None
    #
    x1, y1 = position1
    x2, y2 = position2
    result = abs(x1 - x2) + abs(y1 - y2)
    if mode_dev:
        print_blue("The distance between the two positions is : " + str(result))
    return result
#