LOADED = False
try:
    from aiy.board import Board
    LOADED = True
except ImportError:
    print("Could not load aiy.")

def click_wait():
    if not LOADED: return 1
    with Board() as board:
        board.button.wait_for_release()
    return True
