#!/usr/bin/env python3
#
# QUENYA
#
# This file is responsible has the necessary functions to check if there are some special cases that require some manipulation.
# The special cases are: 1. Diphtongs
#                        2. Consonant clusters
#                        3. Some single consonants (h, s, y)
#                        3. Vowels (check if telco is necessary or not)
#
# --------------Elimina:----------------------
# INPUT:
#           string consisting of a single word
# OUTPUT:
#           True: if there are spacial cases
#           Flase: else

consonant_clusters = {"qu", "nd", "mb", "ng", "ngw", "hw", "nt", "mp", "nc", "nqu", "nw", "rd", "ld", "ss", "hl", "hr"}
diphtongs = {"ai", "oi", "ui", "iu", "eu", "au"}
single_consonants = {"h", "s", "y"}
vowels = {"a", "e", "i", "o", "u", "á", "é", "í", "ó", "ú"}

clusters = consonant_clusters | diphtongs # union of sets

def single_checker(word):
    """
    Check if there are some special single letters
    """
    for letter in single_consonants:
        if letter in word:
            return True

def cluster_checker(word):
    """
    Check if there are some cluster or diphtong in the word
    """
    for cluster in clusters:
        if cluster in word:
            return True

def checker(word):
    """
    Check if the word has either a cluster or a special letter
    """
    if single_checker(word) == True or cluster_checker(word) == True:
        return True

    return False
