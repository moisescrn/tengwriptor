#!/usr/bin/venv python3
#
# QUENYA
#
# INPUT:
#       string (single word)
# OUTPUT:
#       string (transcribed to tengwarscript)

from special_cases_converter import cluster_converter
from special_cases_checker import checker as cluster_checker

letters_dict = {
    "Q" : "\\Tquesse",
    "d" : "\\Tando",
    "b" : "\\Tumbar",
    "g" : "\\Tanga",
    "G" : "\\Tungwe",
    "<" : "\\Thwesta",
    "T" : "\\Tanto",
    "P" : "\\Tampa",
    "C" : "\\Tanca",
    "%" : "\\Tunque",
    "W" : "\\Tnwalme",
    "&" : "\\Tarda",
    "€" : "\\Talda",
    "S" : "\\Tessenuquerna",
    "=" : "\\Thalla\\Tlambe",
    ">" : "\\Thalla\\Troomen",
    "Á" : "\\Tyanta\\TTthreedots",
    "Ó" : "\\Tyanta\\TTrightcurl",
    "Ú" : "\\Tyanta\\TTleftcurl",
    "Ì" : "\\Tuure\\TTdot",
    "È" : "\\Tuure\\TTacute",
    "À" : "\\Tuure\\TTthreedots",
    "a" : "\\TTthreedots",
    "e" : "\\TTacute",
    "i" : "\\TTdot",
    "o" : "\\TTrightcurl",
    "u" : "\\TTleftcurl"
}

def transcriber(word):
    """
    Converts the original word to the tengwarscript commands
    """
    word = word.lower()
    transcribed = ""
    
    if cluster_checker(word) == True:
        word = cluster_converter(word)

    for char in word:
        transcribed += letters_dict[char]

    return transcribed


if __name__ == "__main__":
    word = input("write a word ")
    new = transcriber(word)
    print(new)
