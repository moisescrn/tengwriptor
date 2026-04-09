#!/usr/bin/venv python3
#
# BELERIAND (Sindarin full mode)
#
# INPUT:
#       string (single word)
# OUTPUT:
#       string (transcribed to tengwarscript)

from .special_cases_converter import cluster_converter
from .special_cases_checker import checker as cluster_checker
from .iwng_converter import iwng_converter
from .letters import letters_dict, numbers, numbers_to_duodec
from .base10_to_base12 import base12_converter

def word_transcriber(word, num="duodec"):
    """
    Converts the original word to the tengwarscript commands
    num determines if the numbers will be written in decimal or in duodecimal system
    """
    word = word.lower()

    # check if it is a number
    if word[0] in numbers:
        if num == "duodec":
            # firstly convert to duodecimal
            word = base12_converter(int(word))
            new_word = ""
            for char in word:
                new_word += numbers_to_duodec[char]
            word = new_word

        # invert order for numbers
        word = word[::-1]

    # convert
    transcribed = ""

    if cluster_checker(word) == True:
        word = cluster_converter(word)

    word = iwng_converter(word)

    for char in word:
        transcribed += letters_dict[char]

    return transcribed
