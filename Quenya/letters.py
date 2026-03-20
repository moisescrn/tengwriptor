#!/usr/bin/env python3
# 
# QUENYA
#
# This file defines all different sets of variables that are used within the language of Quenya
# From vowels to consonants and clusters, and conversion dictionaries


# ------- VOWELS -------
non_accent = {"a", "e", "i", "o", "u"}
accent = {"á", "é", "í", "ó", "ú"}
doubled_acc_vowels = {"é", "ó", "ú"}

vowels = non_accent | accent

# vowels where silme and esse have to be transfromed/inverted
nuquerna_vowels = non_accent | doubled_acc_vowels

# Map accented vowels to unaccented, needed to add the aara
normalize = {
    "á" : "a",
    "é" : "e",
    "í" : "i",
    "ó" : "ó",
    "ú" : "u"
}


# ------- Clusters -------

consonant_clusters = {"qu", "nd", "mb", "ng", "ngw", "hw", "nt", "mp", "nc", "nqu", "nw", "rd", "ld", "ss", "hl", "hr", "hy", "rr", "mm", "nn", "tt", "cc", "pp", "ll", "my", "ny", "ry", "ly", "ty", "py", "cy"}
diphtongs = {"ai", "oi", "ui", "iu", "eu", "au"}

clusters = consonant_clusters | diphtongs

single_consonants = {"h", "s", "y"} # used in special_cases_checker

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

# ------- NUMBERS -------
numbers = {"0", "1", "2", "3", "4", "5", "6", "7", "8", "9"}

# ------- CHARACTER CONVERSION -------
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
    "R" : "\\Troomen\\TTdoubler",
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
    "M" : "\\Tmalta\\TTdoubler",
    "N" : "\\Tnuumen\\TTdoubler",
    "T" : "\\Ttinco\\TTdoubler",
    "C" : "\\Tcalma\\TTdoubler",
    "P" : "\\Tparma\\TTdoubler",
    "L" : "\\Tlambe\\TTdoubler",
    "m̀" : "\\Tmalta\\TTtwodotsbelow",
    "ǹ" : "\\Tnuumen\\TTtwodotsbelow",
    "ŕ" : "\\Troomen\\TTtwodotsbelow",
    "ĺ" : "\\Tlambe\\TTtwodotsbelow",
    "ÿ" : "\\Tcalma\\TTtwodotsbelow",
    "ý" : "\\Tparma\\TTtwodotsbelow",
    "ẅ" : "\\Tcalma\\TTtwodotsbelow",
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
    "é" : "\\TTdoubleacute",
    "ó" : "\\TTdoublerightcurl",
    "ú" : "\\TTdoubleleftcurl",
    "|" : "\\Ttelco",
    "^" : "\\Taara",
    "~" : "\\Trighthook",
    "," : "\\Tcentereddot",
    ":" : "\\Tthreeverticaldots",
    ";" : "\\Tcolon",
    "." : "\\Tcolon\\Tcentereddot",
    "!" : "\\raisebox{-0.5ex}{\\tengmag{1.1}\\Texclamation\\tengmag{1}}",
    "?" : "\\tengmag{1.1}\\Tquestion\\tengmag{1}",
    "(" : "\\raisebox{0.5ex}{\\tengmag{1.1}\\rotatebox[origin=c]{180}{\\Tparenthesis}\\tengmag{1}}",
    ")" : "\\tengmag{1.1}\\Tparenthesis\\tengmag{1}",
    "-" : "\\Tcenteredtilde",
    "0" : "\\Tzero\\TTdecimal",
    "1" : "\\Tone\\TTdecimal",
    "2" : "\\Ttwo\\TTdecimal",
    "3" : "\\Tthree\\TTdecimal",
    "4" : "\\Tfour\\TTdecimal",
    "5" : "\\Tfive\\TTdecimal",
    "6" : "\\Tsix\\TTdecimal",
    "7" : "\\Tseven\\TTdecimal",
    "8" : "\\Teight\\TTdecimal",
    "9" : "\\Tnine\\TTdecimal"
}
