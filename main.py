#!/usr/bin/env python3
from sayings import Sayings
from text import TextDB
from tts import speak
from bonnet import click_wait, set_colour, Col


def speak_status(textdb: TextDB, sayings: Sayings, lang: str):
    set_colour(Col.ACTIVE)
    speak(sayings.time_greeting(), lang)
    speak(textdb.get_text("prestatus"), lang)

    set_colour(Col.WORKING)
    corona = sayings.coronastatus()
    set_colour(Col.ACTIVE)
    speak(corona, lang)

    set_colour(Col.WORKING)
    news = sayings.news()
    for saying in news:
        set_colour(Col.ACTIVE)
        speak(saying, lang)
    speak(textdb.get_text("poststatus"), lang)

def main():
    lang = "da"
    textdb = TextDB(lang)
    sayings = Sayings(textdb)

    set_colour(Col.ACTIVE)
    speak(textdb.get_text("booted"), lang)
    while True:
        set_colour(Col.WAIT)
        print("Ready! Waiting for press")

        # Code halts here
        click_wait()
        print("Clicked!")

        try:
            speak_status(textdb, sayings, lang)
        except Exception as e:
            print("ERROR")
            print(e)
            speak(textdb.get_text("speakerror"), lang)

if __name__ == '__main__':
    set_colour(Col.BOOT)
    print("Booting ...")
    main()
