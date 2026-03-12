#!/usr/bin/ven python3
# 
# Takes a file as input and generates a .tex file that can be compiled to give the transcribed version
# https://stackoverflow.com/questions/22846858/python-pass-arguments-to-a-script

import sys
from Quenya import word_transcriber
from Splitter import words_splitter

#text_to_transcribe = sys.argv[0]

splitted_text = words_splitter.splitter("text.txt")
file = open("tran.tex","w")
file.write("\\documentclass{article}\n\\usepackage[annatar]{tengwarscript}\n\\pdfmapfile{=tengwarscript.map}\n\\pagenumbering{gobble}\n\\begin{document}\n")

paragraph = ""
for paragr_num in range(len(splitted_text)):
    for word in splitted_text[paragr_num]:
        paragraph += word_transcriber.word_transcriber(word) + "\\Ts"
    file.write("\n")
    file.write(paragraph)
    file.write("\n")
    paragraph = ""

file.write("\n\\end{document}")
file.close()
