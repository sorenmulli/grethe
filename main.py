#!/usr/bin/env python3
from text import TextDB
from tts import speak
from bonnet import click_wait


def main():
    lang = "da"
    textdb = TextDB(lang)

    while True:
        print("Ready! Waiting for press")
        if click_wait():
            print("Clicked!")
            speak(textdb.get_text("hello"), lang)

if __name__ == '__main__':
    print("Booting ...")
    main()
