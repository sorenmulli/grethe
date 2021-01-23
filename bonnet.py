from enum import Enum

LOADED = False

try:
    from aiy.board import Board
    from aiy.leds import Leds
except ImportError:
    print("WARNING: Could not load aiy. You can still run in debug mode")

class Bonnet:
    """Communication with bonnet button led and bonnet microphone"""

    col_boot    = (255, 153, 0)    # Orange
    col_wait    = (102, 255, 204)  # Turqouis
    col_working = (102, 0, 255)    # Purple
    col_speak   = (255, 102, 255)  # Pink

    def __init__(self):
        self.leds = Leds()
        self.board = Board()

        self.current_col = None

    def wait_for_button(self):
        self.board.button.wait_for_release()

    def set_colour(self, col: tuple):
        self.leds.update(Leds.rgb_on(col))
        self.current_col = col
