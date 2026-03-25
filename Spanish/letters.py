#!/usr/bin/env python3
# 
# ESPAÑOL
#
# This file defines all different sets of variables that are used within the language of Spanish
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
    "ó" : "o",
    "ú" : "u"
}


# ------- Clusters -------

consonant_clusters = {"qu", "nd", "mb", "nǵ", "nt", "mp", "nk", "nz", "rd", "ld", "rr", "tt", "kz", "mm", "nn", "pp", "ll", "kh"}
# Strange things: the cg converter will be applied before the clusters are revised
# Therefore we  have kz instead of cc, kh instead of kh, or nǵ instead of ng. Note that nj is no cluster
diphtongs = {"ai", "ei", "oi", "ui", "iu", "eu", "au", "ou", "ia", "ie", "io", "ua", "ue", "uo"} # Transcription of additional diphtongs inspired by https://www.omniglot.com/conscripts/tengwares.php

clusters = consonant_clusters | diphtongs

single_consonants = {"h", "s", "y"} # used in special_cases_checker

cluster_dict = {
    "rr" : "R",
    "qu" : "k",
    "nd" : "D",
    "mb" : "B",
    "nǵ" : "G",
    "nt" : "ń",
    "mp" : "ṕ",
    "nk" : "ć",
    "nz" : "%",
    "rd" : "&",
    "ld" : "€",
    "mm" : "M",
    "nn" : "N",
    "tt" : "T",
    "kz" : "C",
    "pp" : "P",
    "ll" : "L",
    "kh" : "H",
    "ai" : "Á",
    "ei" : "É",
    "oi" : "Ó",
    "ui" : "Ú",
    "iu" : "Ì",
    "eu" : "È",
    "au" : "À",
    "ou" : "Ò",
    "ia" : "ï",
    "ua" : "ü",
    "ie" : "ë",
    "ue" : "Ü",
    "io" : "Ï",
    "uo" : "Ö"
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
    "t" : "\\Ttinco",
    "d" : "\\Tando",
    "p" : "\\Tparma",
    "b" : "\\Tumbar",
    "z" : "\\Tthuule",
    "k" : "\\Tcalma",
    "ǵ" : "\\Tanga",
    "f" : "\\Tformen",
    "n" : "\\Tnuumen",
    "m" : "\\Tmalta",
    "ñ" : "\\Tnoldo",
    "r" : "\\Toore",
    "v" : "\\Tvala",
    "w" : "\\Tvilya",
    "y" : "\\Tanna\\TTtwodotsbelow",
    "l" : "\\Tlambe",
    "s" : "\\Tsilme",
    "ś" : "\\Tsilmenuquerna",
    "x" : "\\Tquesse\\Tlefthook",
    "h" : "\\Taha",
    "j" : "\\Thyarmen",
    "R" : "\\Troomen",
    "Q" : "\\Tquesse",
    "D" : "\\Tando\\TTdoubler",
    "B" : "\\Tumbar\\TTdoubler",
    "G" : "\\Tanga\\TTdoubler",
    "ń" : "\\Tanto",
    "ṕ" : "\\Tampa",
    "ć" : "\\Tanca",
    "%" : "\\Tthuule\\TTdoubler",
    "&" : "\\Tarda",
    "€" : "\\Talda",
    "M" : "\\Tmalta\\TTdoubler",
    "N" : "\\Tnuumen\\TTdoubler",
    "T" : "\\Ttinco\\TTdoubler",
    "C" : "\\Tthuule\\TTverticalbarbelow",
    "P" : "\\Tparma\\TTdoubler",
    "L" : "\\Tanna\\TTtwodotsbelow",
    "H" : "\\Taha",
    "Á" : "\\Tyanta\\TTthreedots",
    "É" : "\\Tyanta\\TTacute",
    "Ó" : "\\Tyanta\\TTrightcurl",
    "Ú" : "\\Tyanta\\TTleftcurl",
    "Ì" : "\\Tuure\\TTdot",
    "È" : "\\Tuure\\TTacute",
    "À" : "\\Tuure\\TTthreedots",
    "Ò" : "\\Tuure\\TTrightcurl",
    "ï" : "\\Ttelco\\TTthreedots\\TTdotbelow",
    "ü" : "\\Ttelco\\TTthreedots\\TTleftcurlbelow",
    "ë" : "\\Ttelco\\TTacute\\TTdotbelow",
    "Ü" : "\\Ttelco\\TTacute\\TTleftcurlbelow",
    "Ï" : "\\Ttelco\\TTrightcurl\\TTdotbelow",
    "Ö" : "\\Ttelco\\TTrightcurl\\TTleftcurlbelow",
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
    "¡" : "\\raisebox{-0.5ex}{\\tengmag{1.1}\\rotatebox[origin=c]{180}{\\Texclamation}\\tengmag{1}}",
    "?" : "\\tengmag{1.1}\\Tquestion\\tengmag{1}",
    "¿" : "\\tengmag{1.1}\\rotatebox[origin=c]{180}{\\Tquestion}\\tengmag{1}",
    "(" : "\\raisebox{0.5ex}{\\tengmag{1}\\rotatebox[origin=c]{180}{\\Tparenthesis}\\tengmag{1}}",
    ")" : "\\tengmag{1}\\Tparenthesis\\tengmag{1}",
    "-" : "\\Tcenteredtilde",
    "\"" : "\\Tromandblquoteright",
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
