#!/usr/bin/venv python3
# 
# QUENYA
#
# This file contains functions that convert the letters h, s and r

from letters import vowels, nuquerna_vowels

def hsr_converter(word):
    """
    Handles with the special cases of h, s and r
    At beginning of word: h -> j
    At end of word: s -> ~
    Before consonants: r -> @
    Before vowels: s -> ś, ss -> Ś, at this point ss will be S!!
    """
    # convert h
    if word[0] == "h":
        if word[1] != "y" and word[1] != "r" and word[1] != "l":
            word = "j" + word[1:]

    # convert final s
    if word[-1] == "s":
        word = word[:-1] + "~"

    # convert r
    for i in range(len(word)):
        if word[i] == "r":
            # at the end of the word
            if i == len(word)-1:
                word = word[:-1] + "@"

            # before consonants
            elif word[i+1] not in vowels|{"|","^"}:
                word = word[:i] + "@" + word[i+1:]

    # convert s and ss
    # we dont need to consider diphtongs because this function will be called after the vowels are property transformed
    # at this point ss is writen as S
    for i in range(len(word)):
        if word[i] == "s" and word[i+1] in nuquerna_vowels:
            word = word[:i] + "ś" + word[i+1:]
            
        if word[i] == "S" and word[i+1] in nuquerna_vowels:
            word = word[:i] + "Ś" + word[i+1:]

    return word
