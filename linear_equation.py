def calculate_x(y, m, c):
    """
    Calculate the value of x given y = mx + c equation.

    Args:
    y (float): The y-coordinate.
    m (float): The slope of the line.
    c (float): The y-intercept of the line.

    Returns:
    float: The value of x.
    """
    return (y - c) / m
