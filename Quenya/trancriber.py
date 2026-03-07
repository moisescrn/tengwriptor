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
from vowel_preparation import vowel_preparation

letters_dict = {
    "t" : "\\Ttinco",
    "p" : "\\Tparma",
    "c" : "\\Tcalma",
    "k" : "\\Tcalma",
    "f" : "\\Tformen",
    "n" : "\\Tnuumen",
    "m" : "\\Tmalta",
    "r" : "\\Troomen",
    "v" : "\\Tvala",
    "y" : "\\Tanna\\TTtwodotsbelow",
    "l" : "\\Tlambe",
    "s" : "\\Tsilme",
    "ś" : "\\Tsilmenuquerna",
    "x" : "\\Tquesse\\Tlefthook",
    "h" : "\\Taha",
    "H" : "\\Thyarmen\\TTtwodotsbelow",
    "R" : "\\Troomen\\Tdoubler",
    "Q" : "\\Tquesse",
    "d" : "\\Tando",
    "b" : "\\Tumbar",
    "g" : "\\Tanga",
    "G" : "\\Tungwe",
    "<" : "\\Thwesta",
    "ń" : "\\Tanto",
    "ṕ" : "\\Tampa",
    "ć" : "\\Tanca",
    "%" : "\\Tunque",
    "W" : "\\Tnwalme",
    "&" : "\\Tarda",
    "€" : "\\Talda",
    "S" : "\\Tessenuquerna",
    "=" : "\\Thalla\\Tlambe",
    ">" : "\\Thalla\\Troomen",
    "M" : "\\Tmalta\\Tdoubler",
    "N" : "\\Tnuumen\\Tdoubler",
    "T" : "\\Ttinco\\Tdoubler",
    "C" : "\\Tcalma\\Tdoubler",
    "P" : "\\Tparma\\Tdoubler",
    "L" : "\\Tlambde\\Tdoubler",
    "m̀" : "\\Tmalta\\Ttwodotsbelow",
    "ǹ" : "\\Tnuumen\\Ttwodotsbelow",
    "ŕ" : "\\Troomen\\Ttwodotsbelow",
    "ĺ" : "\\Tlambe\\Ttwodotsbelow",
    "ÿ" : "\\Tcalma\\Ttwodotsbelow",
    "ý" : "\\Tparma\\Ttwodotsbelow",
    "ẅ" : "\\Tcalma\\Ttwodotsbelow",
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
    "u" : "\\TTleftcurl",
    "|" : "\\Ttelco",
    "^" : "\\Taara"
}

def transcriber(word):
    """
    Converts the original word to the tengwarscript commands
    """
    word = word.lower()
    transcribed = ""

    if cluster_checker(word) == True:
        word = cluster_converter(word)

    word = vowel_preparation(word)

    for char in word:
        transcribed += letters_dict[char]

    return transcribed


if __name__ == "__main__":
    word = input("write a word ")
    new = transcriber(word)
    print(new)
