import pygame
from libs import pygame_utils
from libs import colors
from libs import xf_coords


def the_map():

    ret = []

    ret.append([()])

    return ret


class Game:
    """
    Holds necessary mutable state and game logic.
    """

    def __init__(self):
        self.config = {}

        # a pygame Surface object, which we'll need to reference in order to draw.
        # None until the window is open.
        self.surface = None

        self.paused = True
        self.state = State()

        self.background_color = colors.CHOCOLATE3
        self.window_width = 1400
        self.window_height = 900

    def open_window(self):
        pygame_utils.init_pygame()
        pygame_utils.set_window_centered()
        pygame_utils.set_window_caption("Game-2")
        self.surface = pygame_utils.open_window_and_get_surface(self.window_width, self.window_height)

    def update(self, evs, keys_pressed):
        self.state.step += 1

    def draw(self):
        pygame_utils.fill_background(self.surface, self.background_color)

        pygame.draw.circle(self.surface, colors.ALICEBLUE, (self.state.step, self.state.step), self.state.step)

        pygame_utils.flip_display()

    def populate(self):
        self.state.ents.append(Player.init())

    def draw_shape(self, shape):



        pass

    def loop(self):

        running = True

        while running:

            evs = pygame.event.get()
            pressed = pygame.key.get_pressed()

            self.update(evs, pressed)

            self.draw()

            # later we'll have to compute the delay time
            pygame.time.delay(30)

            for ev in evs:
                if ev.type == pygame.QUIT:
                    pygame.display.quit()
                    pygame.quit()
                    running = False


class Player:

    @staticmethod
    def init():
        return {
            "pos": [0, 0],
        }


class State:
    """
    Holds most game state such as entities
    """

    def __init__(self):
        self.step = 0
        self.ents = []

