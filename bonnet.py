from enum import Enum

LOADED = False
try:
    from aiy.board import Board
    from aiy.leds import Leds
    LOADED = True
except ImportError:
    print("Could not load aiy.")

class Col(Enum):
    """
    Predefined colours for button.
    """
    BOOT    = (255, 153, 0)    # Orange
    WAIT    = (102, 255, 204)  # Turqouis
    WORKING = (102, 0, 255)    # Purple
    ACTIVE  = (255, 102, 255)  # Pink



def click_wait():
    if not LOADED: return
    with Board() as board:
        board.button.wait_for_release()
    return True

def set_colour(colour: Col):
    if not LOADED: return
    with Leds() as leds:
        leds.update(Leds.rgb_on(colour))
