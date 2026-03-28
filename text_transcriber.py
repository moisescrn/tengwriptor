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
#   -n ... set desired number system
#   -d ... dark mode
#   -s ... eliminate spaces
#   -p ... set paper size (in cm): paperwidth, paperheight, margin
#   -m ... center the text (put it in the middle)

options = "hcf:o:l:n:dsp:mt"
long_options = {"help", "compile", "font", "outputFile", "language", "numberSystem", "darkStyle", "noSpace", "paperSize", "textMiddle", "transparent"}

# Chivatos, to see if an argument has been set
comp_chiv = 0
font_chiv = 0
output_chiv = 0
lang_chiv = 0
num_chiv = 0
dark_chiv = 0
nospa_chiv = 0
paper_chiv = 0
center_chiv = 0

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
        elif currentArg in {"-n", "--numberSystem"}:
            numsys = Argument_functions.set_numbersystem(currentVal)
            num_chiv += 1
        elif currentArg in {"-d", "--darkStyle"}:
            dark_chiv += 1
        elif currentArg in {"-s", "--noSpace"}:
            nospa_chiv += 1
        elif currentArg in {"-p", "--paperSize"}:
            paper_chiv += 1
            v1, v2, v3 = currentVal.split(",")
        elif currentArg in {"-m", "--textMiddle"}:
            center_chiv += 1
        elif currentArg in {"-t", "--transparent"}:
            dark_chiv += 2

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
if num_chiv == 0:
    numsys = "duodec" 

# ---- Reading and splitting text ----
splitted_text = words_splitter.splitter(text_to_transcribe)

# ---- Trascription ----
file = open(new_file,"w")
# Set paper size
if paper_chiv == 1:
    size = "\\usepackage[paperwidth="+v1+"cm,paperheight="+v2+"cm,margin="+v3+"cm]{geometry}\n"
else:
    size = ""

# Center the text
if center_chiv == 1:
    begin_centering = "\\begin{center}\n"
    end_centering = "\n\\end{center}"
else:
    begin_centering = ""
    end_centering = ""

# Set dark mode
if dark_chiv == 1:
    file.write("\\documentclass{article}\n\\usepackage[" + font + "]{tengwarscript}\n\\pdfmapfile{=tengwarscript.map}\n\\usepackage{graphicx}\n\\pagenumbering{gobble}\n\\usepackage{xcolor}\n\\color{white}\n\\pagecolor{black}\n" + size + "\\begin{document}\n" + begin_centering)
elif dark_chiv == 2:
    file.write("\\documentclass{article}\n\\usepackage[" + font + "]{tengwarscript}\n\\pdfmapfile{=tengwarscript.map}\n\\usepackage{graphicx}\n\\pagenumbering{gobble}\n\\usepackage{xcolor}\n\\color{white}\n\\nopagecolor\n" + size + "\\begin{document}\n" + begin_centering)
else:
    file.write("\\documentclass{article}\n\\usepackage[" + font + "]{tengwarscript}\n\\pdfmapfile{=tengwarscript.map}\n\\usepackage{graphicx}\n\\pagenumbering{gobble}\n" + size + "\\begin{document}\n" + begin_centering)

paragraph = ""
# if no space desired, do not add Ts
if nospa_chiv == 1:
    space = ""
else:
    space = "\\Ts"

for paragr_num in range(len(splitted_text)):
    for word in splitted_text[paragr_num]:
        paragraph += transcr(word, numsys) + space
    file.write("\n")
    file.write(paragraph)
    file.write("\n")
    paragraph = ""

file.write(end_centering + "\n\\end{document}")
file.close()

# If -c has been set, lets compile it
if comp_chiv == 1:
    os.system(f"/usr/local/texlive/2025/bin/x86_64-linux/pdflatex {new_file}")
    # it is better to write the absolute path
    # so will the tengwriptor work also inside other scripts
