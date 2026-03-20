#!/usr/bin/venv python3
# 
# Takes a file as input and generates a .tex file that can be compiled to give the transcribed version

import getopt, sys, os
from Quenya.word_transcriber import word_transcriber as quenya_transcriber
from Spanish.word_transcriber import word_transcriber as spanish_transcriber
from Splitter import words_splitter
import Argument_functions

transcriber_mappings = {
    "quenya" : quenya_transcriber,
    "spanish" : spanish_transcriber
}

# ---- Setting arguments ----
#   -h ... help
#   -c ... autocompile to get pdf automatically
#   -f ... font
#   -o ... name of output file
#   -l ... language

options = "hcf:o:l:"
long_options = {"help", "compile", "font", "outputFile", "language"}

# Chivatos, to see if an argument has been set
comp_chiv = 0
font_chiv = 0
output_chiv = 0
lang_chiv = 0

try:
    arguments, values = getopt.getopt(sys.argv[1:], options, long_options)
    for currentArg, currentVal in arguments:
        if currentArg in {"-h", "--help"}:
            Argument_functions.helpPanel()
            sys.exit(1)
        elif currentArg in {"-c", "--compile"}:
            comp_chiv += 1
        elif currentArg in {"-f", "--font"}:
            font = Argument_functions.set_font(currentVal)
            font_chiv += 1
        elif currentArg in {"-o", "--outputFile"}:
            new_file = Argument_functions.set_outputfile(currentVal)
            output_chiv += 1
        elif currentArg in {"-l", "--language"}:
            transcr = transcriber_mappings[Argument_functions.set_language(currentVal)]
            lang_chiv += 1
except getopt.GetoptError as err:
    print(str(err))
    print("\nPrinting usage instructions:")
    Argument_functions.helpPanel()
    sys.exit(1)

# ------- Default settings -------
# in case some arguments are not given, explicitly we need a default setting
text_to_transcribe = sys.argv[-1]
if font_chiv == 0:
    font = "annatar"
if output_chiv == 0:
    if "." in text_to_transcribe:
        new_file = text_to_transcribe[:-4] + ".tex"
    else:
        new_file = text_to_transcribe + ".tex"
if lang_chiv == 0:
    transcr = quenya_transcriber

# ---- Reading and splitting text ----
splitted_text = words_splitter.splitter(text_to_transcribe)

# ---- Trascription ----
file = open(new_file,"w")
file.write("\\documentclass{article}\n\\usepackage[" + font + "]{tengwarscript}\n\\pdfmapfile{=tengwarscript.map}\n\\usepackage{graphicx}\n\\pagenumbering{gobble}\n\\begin{document}\n")

paragraph = ""
for paragr_num in range(len(splitted_text)):
    for word in splitted_text[paragr_num]:
        paragraph += transcr(word) + "\\Ts"
    file.write("\n")
    file.write(paragraph)
    file.write("\n")
    paragraph = ""

file.write("\n\\end{document}")
file.close()

# If -c has been set, lets compile it
if comp_chiv == 1:
    os.system(f"pdflatex {new_file}")
