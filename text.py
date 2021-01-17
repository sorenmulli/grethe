import os
import sys
import json
import random

class TextDB:
    """ Handler of Fetching text pieces """
    path = os.path.join(sys.path[0], "assets", "textdb")

    def __init__(self, lang: str):
        self.lang = lang

        if not self.lang in os.listdir(self.path):
            raise FileNotFoundError(f"I do not have language files for {lang}")

        self.phrases = dict()
        files = os.listdir(os.path.join(self.path, self.lang))
        for file in files:
            with open(os.path.join(self.path, self.lang, file), "r") as jsonfile:
                phrases = json.load(jsonfile)
            self.phrases = {**self.phrases, **phrases}

    def get_text(self, key: str, randomize: bool=True):
        try:
            phrases = self.phrases[key]
        except KeyError as ke:
            raise KeyError(f"I do not know the phrase with key {key} in the language {self.lang}") from ke

        if len(phrases) > 1 and randomize:
            return random.choice(phrases)
        return phrases[0]

