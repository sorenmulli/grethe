LOADED = False
try:
    import aiy
    LOADED = True
except ImportError:
    print("Could not load aiy.")

def click_wait():
    if not LOADED: return
    b = aiy.board.Button()
    b.wait_for_release()
    return True
