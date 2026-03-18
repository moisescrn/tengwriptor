#!/usr/bin/env python3
# 
# ESPAÑOL
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

consonant_clusters = {"qu", "nd", "mb", "nǵ", "nt", "mp", "nk", "nz", "rd", "ld", "rr", "tt", "kz", "mm", "nn", "pp", "ll", "ch"}
# Strange things: the cg converter will be applied before the clusters are revised
# Therefore we  have kz instead of cc, or nǵ instead of ng. Note that nj is no cluster
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
    "ch" : "H",
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

# ------- LETTERS CONVERSION -------
letters_dict = {
    "t" : "\\Ttinco",
    "p" : "\\Tparma",
    "k" : "\\Tcalma",
    "ǵ" : "\\Tanga",
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
    "R" : "\\Troomen\\TTdoubler",
    "Q" : "\\Tquesse",
    "D" : "\\Tando\\TTnasalizer",
    "B" : "\\Tumbar\\TTnasalizer",
    "G" : "\\Tanga\\TTnasalizer",
    "ń" : "\\Tanto",
    "ṕ" : "\\Tampa",
    "ć" : "\\Tanca",
    "%" : "\\Tthuule\\TTnasalizer",
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
    "!" : "\\Texclamation",
    "?" : "\\Tquestion",
    "(" : "\\Tparenthesis",
    ")" : "\\Tparenthesis",
    "-" : "\\Tcenteredtilde"
}
