# for transforming points and shapes between coordinate systems
import math


# a point from world coordinates to relative camera coords
def world_to_camera_relative(point, cam_pos, cam_deg):

    dist = distance_between(cam_pos, point)
    deg = angle_between(cam_pos, point)

    pass


def delta_x(p0, p1):
    return p0[0] - p1[0]


def delta_y(p0, p1):
    return p0[1] - p1[1]


def angle_between(p0, p1):
    pass


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


