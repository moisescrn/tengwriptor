#!/usr/bin/env python3
#
# ESPAÑOL
#
# This file checks if a vowel needs telco, aara or nothing,
# if needed | or ^ are introduced into the word
# the diphtongs are seen as clusters and therefore are not treated here,
# but in special_case_converter.py

from .letters import diphtongs, vowels, accent, non_accent, doubled_acc_vowels, normalize

def manipulation_checker(word, vowel, position):
    """
    Checks if a specific vowel needs a manipulation or if it can be let as it is
    There are two cases where manipulation is needed:
        1. at beginning of the word, but not inside a diphtong
        2. after another vowel, but not inside a diphtong
    Counter is used in case a vowel appears more than once
    OUTPUT:
        True, manipulation needed
        False, no manipulation needed
    """
    position = int(position)
    if position == 0: # beginning, solves it for any vowel at the beginning, including with accent
        if vowel+word[1] not in diphtongs:
            return True

    elif word[position-1] in vowels and word[position-1]+vowel not in diphtongs: # after another vowel and not in diphtong
        return True

    elif vowel in accent and vowel not in doubled_acc_vowels: # in case we always need an aara
        return True

    return False

def find_position(word):
    """
    Returns a list with the position of the vowels
    e.g.: for "ancalime" we have the vowels ['a', 'a', 'i', 'e']
    and this function returns posit_vow = [0, 3, 5, 7]
    """
    posit_vow = [position for position, letter in enumerate(word) if letter in vowels ]
    return posit_vow

def add_telco_aara(word, break_points):
    """
    telco and aara are lists that contain the position of the letters that need a telco or an aara to be added (so it must be added before that position)
    This function takes word and adds the needed manipulations
    """
    break_points = sorted(break_points) # it should be sorted, but let's go safe
    parts = []

    # Split the word into parts: Whenever we need a telco or aara, we make a break
    parts.append(word[:min(break_points)]) # first part, until the first vowel that needs manipulation
    for j in range(1, len(break_points)): # begin with 1 to avoid an empty string
        parts.append(word[break_points[j-1]:break_points[j]])
    parts.append(word[max(break_points):])

    # Now on each braek we add either a telco or an aara
    # Note that each part, except the first one, begins with the vowel to be manipulated
    new_parts = [parts[0]]
    parts.pop(0) # eliminate the first part to allow the following iteration
    for part in parts:
        if part[0] in non_accent:
            new_parts.append("|" + part)
        elif part[0] in accent:
            norm_vow = normalize[part[0]]
            new_parts.append("^" + norm_vow + part[1:]) # eliminate the vowel with accent and then add it

    # Sum all parts back together
    manip_word = ""
    for part in new_parts:
        manip_word += part

    return manip_word

def vowel_preparation(word):
    """
    If needed the telco and aara characters are introduced
    """
    # Check if the word consists of only one character (always a vowel). if so then return the result
    if len(word) == 1:
        if word in non_accent:
            return "|" + word
        elif word in accent:
            return "^" + normalize[word]
        elif word == "y":
            return "|i"

    posit_vow = find_position(word)

    # take track of the positions where we need a break to add a telco or an aara
    break_points = []
    for position in posit_vow:
        vowel = word[position]
        if manipulation_checker(word, vowel, position) == True:
            break_points.append(position)

    if break_points == []: # it could be possible that we have no break points, so just return the original word
        return word

    # add the necessary manipulation and then just return the final word
    word = add_telco_aara(word, break_points)
    return word
