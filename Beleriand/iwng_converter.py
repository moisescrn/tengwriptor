#!/usr/bin/env python3
#
# BELERIAND (Sindarin full mode)
#
# This file checks is a word begins with an i or if it contains a w

from .letters import vowels

def iwng_converter(word):
    """
    Applies the corresponding transformation
    This transformation happens only if the initial letter is either an i or a w
    """
    if len(word) == 1:
        if word == "i":
            return word
    # check  if i is at beginning of word
    if word[0] == "i" and word[1] in vowels:
        word = "I" + word[1:]
    elif word[0] in {"í", "î"}:
        word = "Í" + word[1:]
    # check if w is at beginning of word
    elif word[0] == "w":
        word = "W" + word[1:]
    # check if ng is at beginning of word
    elif word[0] == "ǵ":
        word = "G" + word[1:]

    # check if ng at end of word
    if word[-1] == "ǵ":
        word = word[:-1] + "G"

    return word
