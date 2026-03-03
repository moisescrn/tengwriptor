#!/usr/bin/env python3
#
# QUENYA
#
# This file checks if a vowel needs telco, aara or nothing,
# if needed | or ^ are introduced into the word
# the diphtongs are seen as clusters and therefore are not treated here,
# but in special_case_converter.py

non_accent = {"a", "e", "i", "o", "u"}
accent = {"á", "é", "í", "ó", "ú"}
diphtongs = {"ai", "oi", "ui", "iu", "eu", "au"}
not_aara_vowels = {"é", "ó", "ú"}

vowels = non_accent | accent

# Map accented vowels to unaccented, needed to add the aara
normalize = {
    "á" : "a",
    "é" : "e",
    "í" : "i",
    "ó" : "ó",
    "ú" : "u"
}

def manipulation_checker(word, vowel):
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
    position = word.index(vowel)

    if position == 0: # beginning, solves it for any vowel at the beginning, including with accent
        if vowel+word[1] not in diphtongs:
            return True

    elif word[position-1] in vowels and word[position-1]+vowel not in diphtongs: # after another vowel and not in diphtong
        return True
    
    if vowel in accent and vowel not in not_aara_vowels: # in case we always need an aara
        return True

    return False

def extract_vowels(word):
    """
    Returns in a list all vowels that appear in the input word
    """
    list_vow = []
    for letter in word:
        if letter in vowels:
            list_vow.append(letter)
    return list_vow

def vowel_preparation(word):
    """
    If needed the telco and aara characters are introduced
    """
    list_vow = extract_vowels(word)

    for vowel in list_vow:
        if manipulation_checker(word, vowel) == True:
            if vowel in non_accent:
                word = word.replace(vowel, "|" + vowel)
            elif vowel in accent:
                word = word.replace(vowel, "^" + normalize[vowel])

    return word

if __name__ == "__main__":
    word = input("write a word ")
    vowel = input("write a vowel ")
    done_result = vowel_preparation(word)
    list_result = extract_vowels(word)
    result = manipulation_checker(word, vowel)
    print(result)
    print(list_result)
    print(done_result)
