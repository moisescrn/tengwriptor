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

def cg_converter(word):
    """
    Prepares c and g depending on the pronounciation
    c -> k
    c -> z (before e, i)
    g -> ǵ
    g -> j (before e, i)
    """
    # Begin handling with the special case of ending with g or c
    if word[-1] == "c":
        word = word[:-1] + "k"
    elif word[-1] == "g":
        if word[-2] != "n":
            word = word[:-1] + "ǵ"
        else:
            word = word[:2] + "G"

    for i in range(len(word)):
        # Convert c
        if word[i] == "c":
            if word[i+1] in {"e", "i"}:
                word = word[:i] + "z" + word[i+1:]
            else:
                word = word[:i] + "k" + word[i+1:]
        # Convert g
        elif word[i] == "g":
            if word[i+1] in {"e", "i"}:
                word = word[:i] + "j" + word[i+1:]
            elif word[i+1] == "u" and word[i+2] in {"e", "i"}:
                word = word[:i] + "ǵ" + word[i+1:]
            else:
                word = word[:i] + "ǵ" + word[i+1:]
    # in case we have ǵu we still have to eliminate the u
    # this is necessary to let the for-loop run correctly
    if "ǵue" in word or "ǵui" in word:
        word = word.replace("ǵu", "ǵ")
    # Es importante hacer esto en este punto
    if "ü" in word:
        word = word.replace("ü", "u")

    return word
