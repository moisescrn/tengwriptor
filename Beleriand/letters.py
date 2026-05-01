#!/usr/bin/env python3
# 
# BELERIAND (Sindarin full mode)
#
# This file defines all different sets of variables that are used within the language of Quenya
# From vowels to consonants and clusters, and conversion dictionaries


# ------- VOWELS -------
non_accent = {"a", "e", "i", "o", "u"}
accent = {"á", "é", "í", "ó", "ú"}

vowels = non_accent | accent

# ------- Clusters -------

consonant_clusters = {"th", "ph", "ch", "dh", "nn", "mm", "rh", "lh", "ss", "ll", "rr", "hw", "nt", "nd", "mp", "mb", "nk", "ng"}
diphtongs = {"ae", "oe", "ai", "ei", "ui", "au", "aw"}

clusters = consonant_clusters | diphtongs

cluster_dict = {
    "th" : "T",
    "ph" : "f",
    "ch" : "C",
    "dh" : "D",
    "nn" : "N",
    "mm" : "M",
    "rh" : "ŕ",
    "lh" : "ĺ",
    "ss" : "S",
    "ll" : "L",
    "rr" : "R",
    "hw" : "W",
    "nt" : "ń",
    "nd" : "ǹ",
    "mp" : "ḿ",
    "mb" : "B",
    "nk" : "ć",
    "ng" : "ǵ",
    "ae" : "Á",
    "oe" : "Ó",
    "ai" : "À",
    "ei" : "È",
    "ui" : "Ù",
    "au" : "Ú",
    "aw" : "Ú"
}

# ------- NUMBERS -------
numbers = {"0", "1", "2", "3", "4", "5", "6", "7", "8", "9"}
numbers_to_duodec = {
    "0" : "Z",
    "1" : "µ",
    "2" : "ẗ",
    "3" : "ĸ",
    "4" : "ð",
    "5" : "$",
    "6" : "ſ",
    "7" : "ŧ",
    "8" : "ø",
    "9" : "æ",
    "§" : "§",
    "þ" : "þ"
}
# ------- CHARACTER CONVERSION -------
letters_dict = {
    "T" : "\\Tthuule",
    "C" : "\\Taha",
    "D" : "\\Tanto",
    "N" : "\\Tnuumen",
    "M" : "\\Tmalta",
    "ŕ" : "\\Tarda",
    "ĺ" : "\\Talda",
    "S" : "\\Tesse",
    "L" : "\\Tlambe\\Tlambe",
    "R" : "\\Troomen\\Troomen",
    "W" : "\\Thwestasindarinwa",
    "ń" : "\\Ttinco\\TTnasalizer",
    "ǹ" : "\\Tando\\TTnasalizer",
    "ḿ" : "\\Tparma\\TTnasalizer",
    "B" : "\\Tumbar\\TTnasalizer",
    "ć" : "\\Tcalma\\TTnasalizer",
    "ǵ" : "\\Tanga\\TTnasalizer",
    "G" : "\\Tnoldo", # ng at beginning and end of word
    "Á" : "\\Tosse\\hspace{-5pt}{\\raisebox{+1.5ex}{\\rotatebox[origin=c]{180}{\\TTcaron}}}\\hspace{5pt}",
    "Ó" : "\\Tanna\\hspace{-6.5pt}{\\raisebox{+1.5ex}{\\rotatebox[origin=c]{180}{\\TTcaron}}}\\hspace{6.5pt}",
    "À" : "\\Tosse\\TTtwodots",
    "È" : "\\Tyanta\\TTtwodots",
    "Ù" : "\\Tuure\\TTtwodots",
    "Ú" : "\\Tosse\\TTtilde",
    "t" : "\\Ttinco",
    "p" : "\\Tparma",
    "c" : "\\Tcalma",
    "k" : "\\Tcalma",
    "d" : "\\Tando",
    "b" : "\\Tumbar",
    "g" : "\\Tanga",
    "f" : "\\Tformen",
    "v" : "\\Tampa",
    "n" : "\\Toore",
    "m" : "\\Tvala",
    "W" : "\\Tvilya",
    "w" : "\\TTtilde",
    "r" : "\\Troomen",
    "l" : "\\Tlambe",
    "s" : "\\Tsilme",
    "y" : "\\Tsilmenuquerna",
    "h" : "\\Thyarmen",
    "a" : "\\Tosse",
    "e" : "\\Tyanta",
    "i" : "\\Ttelco",
    "I" : "\\Taara",
    "o" : "\\Tanna",
    "u" : "\\Tuure",
    "á" : "\\Tosse\\TTacute",
    "é" : "\\Tyanta\\TTacute",
    "í" : "\\Ttelco\\TTacute",
    "Í" : "\\Taara\\TTacute",
    "ó" : "\\Tanna\\TTacute",
    "ú" : "\\Tuure\\TTacute",
    "â" : "\\Tosse\\TTacute",
    "ê" : "\\Tyanta\\TTacute",
    "î" : "\\Ttelco\\TTacute",
    "ô" : "\\Tanna\\TTacute",
    "û" : "\\Tuure\\TTacute",
    "/" : "\\raisebox{-0.7ex}{\\tengmag{1.3}\\rotatebox[origin=c]{-15}{\\Thalla}\\tengmag{1}}",
    "," : "\\Tcentereddot",
    ":" : "\\Tthreeverticaldots",
    ";" : "\\Tcolon",
    "." : "\\Tcolon\\Tcentereddot",
    "!" : "\\raisebox{-0.5ex}{\\tengmag{1.1}\\Texclamation\\tengmag{1}}",
    "?" : "\\tengmag{1.1}\\Tquestion\\tengmag{1}",
    "(" : "\\raisebox{0.5ex}{\\tengmag{1.1}\\rotatebox[origin=c]{180}{\\Tparenthesis}\\tengmag{1}}",
    ")" : "\\tengmag{1.1}\\Tparenthesis\\tengmag{1}",
    "-" : "\\Tcenteredtilde",
    "’" : "\\Tromanquoteright",
    "'" : "\\Tromanquoteright",
    "\"" : "\\Tromandblquoteright",
    "[" : "\\Tromandblquoteleft",
    "0" : "\\Tzero\\TTdecimal",
    "1" : "\\Tone\\TTdecimal",
    "2" : "\\Ttwo\\TTdecimal",
    "3" : "\\Tthree\\TTdecimal",
    "4" : "\\Tfour\\TTdecimal",
    "5" : "\\Tfive\\TTdecimal",
    "6" : "\\Tsix\\TTdecimal",
    "7" : "\\Tseven\\TTdecimal",
    "8" : "\\Teight\\TTdecimal",
    "9" : "\\Tnine\\TTdecimal",
    "Z" : "\\Tzero\\TTduodecimal",
    "µ" : "\\Tone\\TTduodecimal",
    "ẗ" : "\\Ttwo\\TTduodecimal",
    "ĸ" : "\\Tthree\\TTduodecimal",
    "ð" : "\\Tfour\\TTduodecimal",
    "$" : "\\Tfive\\TTduodecimal",
    "ſ" : "\\Tsix\\TTduodecimal",
    "ŧ" : "\\Tseven\\TTduodecimal",
    "ø" : "\\Teight\\TTduodecimal",
    "æ" : "\\Tnine\\TTduodecimal",
    "§" : "\\Tten\\TTduodecimal",
    "þ" : "\\Televen\\TTduodecimal"
}
