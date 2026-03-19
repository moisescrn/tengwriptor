#!/usr/bin/venv python3
#
# ESPAÑOL
#
# INPUT:
#       string (single word)
# OUTPUT:
#       string (transcribed to tengwarscript)

from .special_cases_converter import cluster_converter
from .special_cases_checker import checker as cluster_checker
from .vowel_preparation import vowel_preparation
from .h_s_r_c_g_converter import hs_converter, cgr_converter
from .letters import letters_dict

def word_transcriber(word):
    """
    Converts the original word to the tengwarscript commands
    """
    word = word.lower()
    transcribed = ""

    word = cgr_converter(word)

    if cluster_checker(word) == True:
        word = cluster_converter(word)

#    word = vowel_preparation(word)

    word = hs_converter(word)

    word = vowel_preparation(word)

    for char in word:
        transcribed += letters_dict[char]

    return transcribed
