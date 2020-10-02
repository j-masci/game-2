import math


def angle_between(p0, p1):
    """
    >>> round(angle_between([0,0], [0,1]), 2)
    3.14
    """
    return math.atan2(delta_y(p0,p1), delta_x(p0,p1))


def distance_between(p0, p1):
    """
    >>> round(distance_between([0, 0], [0, 0]), 1)
    0.0
    >>> round(distance_between([0, 0], [1, 1]), 2)
    1.41
    >>> round(distance_between([0, 0], [3, 4]), 1)
    5.0
    """
    dx = delta_x(p0, p1)
    dy = delta_y(p0, p1)

    return math.sqrt(dx * dx + dy * dy)


def delta_x(p0, p1):
    return p1[0] - p0[0]


def delta_y(p0, p1):
    return p1[1] - p0[1]


def to_deg(rad):
    """
    >>> round(to_deg(3.14159), 1)
    180.0
    """
    return rad * 180 * (1/math.pi)


def to_rad(deg):
    """
    >>> round(to_rad(180), 2)
    3.14
    """
    return deg * math.pi / 180

