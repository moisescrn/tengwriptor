#!/usr/bin/env python3
#
# BELERIAND (Sindarin full mode)
#
# This file is responsible has the necessary functions to check if there are some special cases that require some manipulation.
# The special cases are: 1. Diphtongs
#                        2. Consonant clusters

from .letters import clusters

def checker(word):
    """
    Check if there are some cluster or diphtong in the word
    """
    for cluster in clusters:
        if cluster in word:
            return True

    return False
