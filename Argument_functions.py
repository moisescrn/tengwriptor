#!/usr/bin/venv python3
#
# Defines the functions that are used in text_transcriber to allow the script
# to take arguments, to modify the script behaviour

import sys

def helpPanel():
    print("\nNAME")
    print("\ttext_transcriber.py - applies the transcription from lating alphabet to tengwar\n")
    print("DESCRIPTION")
    print("\tThis script is responsible to apply the transcription to tengwar, changing the mode as needed depending on the language. The output is a .tex-file that has to be compiled to get the transcription\n")
    print("OPTIONS")
    print("\tThe script accepts the following options:\n")
    print("\t-h, --help \t\t Prints this information panel")
    print("\t-c, --compile \t\t The output .tex-file is compiled automatically")
    print("\t-f, --font \t\t The font can be chosen arbitrary. The default font is 'annatar', in case the given one is invalid, or none is given")
    print("\t-o, --outputFile \t Defines the name of the output file. The default name will be the name of the input file, interchanging the ending by '.tex'")
    print("\t-l, --language \t\t Set the language in which the text is written, so the transcription can be performed correctly. The default language is Quenya\n")
    print("\t-n, --numberSystem \t\t Set the desired number systems to be used, between decimal and duodecimal. The default number system is duodecimal")

def set_font(font):
    """
    Checks if the font given is valid. If not the default font 'anatar' will be set
    """
    fonts = {"annatar", "annataritalic", "annatarbold", "annatarbolditalic",
             "noldor", "noldorcapI", "noldorcapII",
             "quenya", "quenyacapI", "quenyacapII",
             "sindarin", "sindarincapI", "sindarincapII",
             "teleri", "formal",
             "parmaite", "unicodeparmaite",
             "elfica", "gothika"}
    if font not in fonts:
        print("Invalid font, annatar will be used")
        return "annatar"
    else:
        return font

def set_outputfile(file_name):
    """
    Prints the name of the output file
    """
    return file_name

def set_language(language):
    """
    Checks and sets the language.
    For the moment there is only one language, so lets just print the name
    In the future this will be changed
    """
    languages = {"quenya", "sindarin", "spanish", "english"}

    if language not in languages:
        print("Invalid language, quenya will be used")
        return "quenya"
    else:
        return language

def set_numbersystem(numsys):
    """
    Checks if the given number system is either decimal or duodecimal
    """
    systems = {"duodec", "dec"}

    if numsys not in systems:
        print("Invalid number system, the numbers will be given in duodecimal")
        return "duodec"
    else:
        return numsys
