from utils.print.print_color import print_red, print_yellow


def calculate_distance2D(point1, point2, mode_dev=False):
#
    """
        This function calculates the distance between two points.
        @param ( tuple ) point1: The first point
        @param ( tuple ) point2: The second point
        @return ( int ): The distance between the two points
    """
    if (point1 is None) or (point2 is None):
    # 
        if mode_dev:
            print_red("The point is None.")
        return None
    # 
    x1, y1 = point1
    x2, y2 = point2
    if mode_dev:
        print_yellow(f"The distance between {point1} and {point2} is : {abs(x1 - x2) + abs(y1 - y2)}")
    return (abs(x1 - x2) + abs(y1 - y2))
#