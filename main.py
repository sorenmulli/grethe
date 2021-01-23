#!/usr/bin/env python3
from argparse import ArgumentParser

from sayings import Sayings
from text import TextDB
from tts import speak
from bonnet import Bonnet

class AssistantApp:
    def __init__(self, lang: str, debug: bool=False):
        self.lang = lang
        self.debug = debug

        self.bonnet = None if self.debug else Bonnet()
        print("Booting ...")
        if not self.debug:
            self.bonnet.set_colour(self.bonnet.col_boot)

        self.textdb = TextDB(self.lang)
        self.sayings = Sayings(self.textdb)


    def run(self):
        self._say("booted")
        while True:
            print("Waiting for press")
            # Code halts here
            if not self.debug:
                self.bonnet.set_colour(self.bonnet.col_wait)
                self.bonnet.wait_for_button()
            print("Clicked!")
            try:
                self._speak_status()
            except Exception as e:
                print(f"ERROR INTERCEPTED: \n{e}")
                self._say("speakerror")

    def _speak_status(self):
        if not self.debug:
            self.bonnet.set_colour(self.bonnet.col_working)
        self._say(text=self.sayings.time_greeting())
        self._say("prestatus")

        corona = self.sayings.coronastatus()
        self._say(text=corona)

        news = self.sayings.news()
        for saying in news:
            self._say(text=saying)
        self._say("poststatus")

    def _say(self, key: str=None, text: str=None):
        if key is not None:
            text = self.textdb.get_text(key)
        if not self.debug:
            old_col = self.bonnet.current_col
            self.bonnet.set_colour(self.bonnet.col_speak)

        speak(text, self.lang)
        if not self.debug:
            self.bonnet.set_colour(old_col)

if __name__ == '__main__':
    parser = ArgumentParser(description="Run the Grethe Voice Assistant")
    parser.add_argument("--lang", help="Set another language than danish, for example, 'en'", default="da")
    parser.add_argument("--debug", help="Enable debug mode where no contact to bonnet is attempted", action="store_true")
    args = parser.parse_args()

    app = AssistantApp(args.lang, debug=args.debug)
    app.run()
