import pygame
import os


def init_pygame():
    pygame.init()
    pygame.font.init()


def set_window_centered():
    os.environ["SDL_VIDEO_CENTERED"] = "1"


def set_window_caption(caption):
    pygame.display.set_caption(caption)


def set_mouse_visibility(bool):
    pygame.mouse.set_visible(bool)


def open_window_and_get_surface(window_width, window_height):
    surface = pygame.display.set_mode((window_width, window_height))
    return surface


# do this before drawing to self.surface
def fill_background(surface, color):
    surface.fill(color)
    return surface


# do this after drawing to self.surface
def flip_display():
    pygame.display.flip()
