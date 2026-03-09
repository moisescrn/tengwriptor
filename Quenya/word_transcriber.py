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
from h_s_r_converter import hsr_converter

letters_dict = {
    "t" : "\\Ttinco",
    "p" : "\\Tparma",
    "c" : "\\Tcalma",
    "k" : "\\Tcalma",
    "f" : "\\Tformen",
    "n" : "\\Tnuumen",
    "m" : "\\Tmalta",
    "r" : "\\Troomen",
    "@" : "\\Toore",
    "v" : "\\Tvala",
    "w" : "\\Tvilya",
    "y" : "\\Tanna\\TTtwodotsbelow",
    "l" : "\\Tlambe",
    "s" : "\\Tsilme",
    "ś" : "\\Tsilmenuquerna",
    "x" : "\\Tquesse\\Tlefthook",
    "h" : "\\Taha",
    "j" : "\\Thyarmen", # at beginning of word
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
    "S" : "\\Tesse",
    "Ś" : "\\Tessenuquerna",
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
    "é" : "\\TTdoubleaccute",
    "ó" : "\\TTdoublerightcurl",
    "ú" : "\\TTdoubleleftcurl",
    "|" : "\\Ttelco",
    "^" : "\\Taara",
    "~" : "\\Trighthook"
}

def word_transcriber(word):
    """
    Converts the original word to the tengwarscript commands
    """
    word = word.lower()
    transcribed = ""

    if cluster_checker(word) == True:
        word = cluster_converter(word)

    word = vowel_preparation(word)

    word = hsr_converter(word)

    for char in word:
        transcribed += letters_dict[char]

    return transcribed


if __name__ == "__main__":
    word = input("write a word ")
    new = word_transcriber(word)
    print(new)
