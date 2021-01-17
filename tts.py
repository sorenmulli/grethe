import io
import time

import pyglet
from gtts import gTTS

pyglet.options["audio"] = ("pulse",)
TICK = 0.2

def speak(words: str, lang: str):
    # Create the sound using gTTS
    with io.BytesIO() as f:
        gTTS(text=words, lang=lang).write_to_fp(f)
        f.seek(0)
        # Create the playback using pyglet
        sound = pyglet.media.load("_.mp3", file=f)
    # Handle playing of the playback
    player = sound.play()
    player.volume = .5
    playtime = player.source.duration
    while (playtime - TICK) > 0:
        pyglet.app.platform_event_loop.dispatch_posted_events()
        pyglet.clock.tick()
        time.sleep(TICK)
        playtime -= TICK
