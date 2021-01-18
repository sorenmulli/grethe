import io
import time

import pyglet
from gtts import gTTS

pyglet.options["audio"] = ("pulse",)
TICK = 0.1
VOLUME = 0.15

def speak(words: str, lang: str, print_: bool=True):
    if print_:
        print(f"\tSaying '{words}'")

    # Create the sound using gTTS
    with io.BytesIO() as f:
        gTTS(text=words, lang=lang).write_to_fp(f)
        f.seek(0)
        # Create the playback using pyglet
        sound = pyglet.media.load("_.mp3", file=f, streaming=False)
    # Handle playing of the playback
    player = sound.play()
    player.volume = VOLUME
    while player.playing:
        pyglet.app.platform_event_loop.dispatch_posted_events()
        pyglet.clock.tick()
        time.sleep(TICK)
