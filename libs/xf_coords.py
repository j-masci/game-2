# functions for converting between different coordinate systems
# ie. world, camera, window.
import math
from libs import vector_utils as vec


def camera_to_window_coords(point, cam_width, cam_height, precision=None):
    """
    >>> camera_to_window_coords([0, 200], 1500, 800, 1)
    (750.0, 200.0)
    """
    x = point[0] + (cam_width / 2)
    y = (cam_height / 2) - point[1]

    if precision is not None:
        x = round(x, precision)
        y = round(y, precision)

    return x, y


# (defn cam->window [point cam-width cam-height]
#   (let [x (point 0)
#         y (point 1)
#         w2 (/ cam-width 2)
#         h2 (/ cam-height 2)]
#     [(+ x w2)
#      (- h2 y)]))

# camera zero deg points in the positive-y direction
def world_to_camera_coords(point, cam_pos, cam_deg, precision=None):
    """
    >>> world_to_camera_coords([2, 2], [1, 1], 0, 1)
    (1.0, 1.0)
    >>> world_to_camera_coords([15, 15], [0, 15], -90, 1)
    (0.0, 15.0)
    >>> world_to_camera_coords([0, 0], [1, 0], 0, 1)
    (-1.0, 0.0)
    """

    dist = vec.distance_between(cam_pos, point)
    angle = vec.angle_between(cam_pos, point)

    _angle = vec.to_rad(vec.to_deg(angle) - cam_deg)

    x = dist * math.cos(_angle)
    y = dist * math.sin(_angle)

    if precision is not None:
        x = round(x, precision)
        y = round(y, precision)

    return x, y
