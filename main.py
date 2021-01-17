#!/usr/bin/env python3
from text import TextDB
from tts import speak


def main():
    lang = "da"
    textdb = TextDB(lang)

    speak(
        textdb.get_text("hello"), lang
    )

if __name__ == '__main__':
    main()
