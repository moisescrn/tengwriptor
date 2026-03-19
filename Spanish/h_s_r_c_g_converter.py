#!/usr/bin/venv python3
# 
# ESPAÑOL
#
# This file contains functions that convert the letters h, s, r, c and g

from .letters import vowels, nuquerna_vowels, accent, normalize

def hs_converter(word):
    """
    Handles with the special cases of h, s and r
    Eliminate h
    At end of word: s -> ~
    Before vowels: s -> ś
    """
    # handle the h
    # the only h that matters is in ch, which will be converted before this function
    # but we have to consider the case, where we have an h between two vowels
    for i in range(1,len(word)-1):
        if word[i] == "h" and word[i-1] in vowels and word[i+1] in vowels:
            if word[i+1] in accent:
                word = word[:i] + "^" + normalize[word[i+1:]]
            else:
                word = word[:i] + "|" + word[i+1:]
    # in the other cases just eliminate the h
    word = word.replace("h","")
    
    # convert final s
    if word[-1] == "s":
        word = word[:-1] + "~"

    # convert s
    # we dont need to consider diphtongs because this function will be called after the vowels are property transformed
    for i in range(len(word)):
        if word[i] == "s" and word[i+1] in nuquerna_vowels:
            word = word[:i] + "ś" + word[i+1:]

    return word

def cgr_converter(word):
    """
    Prepares c and g depending on the pronounciation
    c -> k
    c -> z (before e, i)
    g -> ǵ
    g -> j (before e, i)
    It also changes an initian r to R, so that we get a roomen
    """
    # Checking the r
    if word[0] == "r":
        word = "R" + word[1:]
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
