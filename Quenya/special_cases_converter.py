#!/usr/bin/env python3
#
# QUENYA
#
# This file contains functions that convert the clusters into other (unique) characters to make the final conversion better

consonant_clusters = {"qu", "nd", "mb", "ng", "ngw", "hw", "nt", "mp", "nc", "nqu", "nw", "rd", "ld", "ss", "hl", "hr"}
diphtongs = {"ai", "oi", "ui", "iu", "eu", "au"}

clusters = consonant_clusters | diphtongs

cluster_dict = {
    "qu" : "Q",
    "nd" : "d",
    "mb" : "b",
    "ng" : "g",
    "ngw" : "G",
    "hw" : "<",
    "nt" : "T",
    "mp" : "P",
    "nc" : "C",
    "nqu" : "%",
    "nw" : "W",
    "rd" : "&",
    "ld" : "€",
    "ss" : "S",
    "hl" : "=",
    "hr" : ">",
    "ai" : "Á",
    "oi" : "Ó",
    "ui" : "Ú",
    "iu" : "Ì",
    "eu" : "È",
    "au" : "À"
}

def cluster_converter(word):
    """
    Apply the map defined by the dictionary
    """
    for cluster in clusters:
        word = word.replace(cluster, cluster_dict[cluster])
    return word
