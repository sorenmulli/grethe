#!/usr/bin/env python3
from sayings import Sayings
from text import TextDB
from tts import speak
from bonnet import click_wait


def speak_status(textdb: TextDB, sayings: Sayings, lang: str):
    speak(sayings.time_greeting(), lang)

    speak(textdb.get_text("prestatus"), lang)
    speak(sayings.coronastatus(), lang)
    for saying in sayings.news():
        speak(saying, lang)
    speak(textdb.get_text("poststatus"), lang)

def main():
    lang = "da"
    textdb = TextDB(lang)
    sayings = Sayings(textdb)

    while True:
        print("Ready! Waiting for press")
        speak(textdb.get_text("booted"), lang)
        if click_wait():
            print("Clicked!")
            try:
                speak_status(textdb, sayings, lang)
            except Exception as e:
                print("ERROR")
                print(e)
                speak(textdb.get_text("speakerror"), lang)

if __name__ == '__main__':
    print("Booting ...")
    main()
