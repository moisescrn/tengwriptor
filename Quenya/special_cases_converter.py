#!/usr/bin/env python3
#
# QUENYA
#
# This file contains functions that convert the clusters into other (unique) characters to make the final conversion better

consonant_clusters = {"qu", "nd", "mb", "ng", "ngw", "hw", "nt", "mp", "nc", "nqu", "nw", "rd", "ld", "ss", "hl", "hr", "hy", "rr", "mm", "nn", "tt", "cc", "pp", "ll", "my", "ny", "ry", "ly", "ty", "py", "cy"}
diphtongs = {"ai", "oi", "ui", "iu", "eu", "au"}

clusters = consonant_clusters | diphtongs

cluster_dict = {
    "hy" : "H",
    "rr" : "R",
    "qu" : "Q",
    "nd" : "d",
    "mb" : "b",
    "ng" : "g",
    "ngw" : "G",
    "hw" : "<",
    "nt" : "ń",
    "mp" : "ṕ",
    "nc" : "ć",
    "nqu" : "%",
    "nw" : "W",
    "rd" : "&",
    "ld" : "€",
    "ss" : "S",
    "hl" : "=",
    "hr" : ">",
    "mm" : "M",
    "nn" : "N",
    "tt" : "T",
    "cc" : "C",
    "pp" : "P",
    "ll" : "L",
    "my" : "m̀",
    "ny" : "ǹ",
    "ry" : "ŕ",
    "ly" : "ĺ",
    "ty" : "ÿ",
    "py" : "ý",
    "cy" : "ẅ",
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
