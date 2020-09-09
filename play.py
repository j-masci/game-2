import os

# hides some stdout. Must do early.
os.environ["PYGAME_HIDE_SUPPORT_PROMPT"] = "1"

from app.game import Game
import sys

game = Game()

# best to use interactive prompt, you can analyze game state after closing game window
# and/or start the game up again.
if __name__ == "__main__":

    if '-no-start' not in sys.argv:
        game.open_window()
        game.play()
