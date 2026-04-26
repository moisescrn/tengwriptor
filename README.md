# Tengwriptor - a tengwar transcriber with LaTeX
Tengwriptor is a transcriber from the Latin alphabet to Tengwar, the Elvish letters designed by J.R.R. Tolkien. At the moment the only supported language is Quenya, but in the future more languages like Sindarin, Spanish and English will be implemented.

# Prerequisites
The project is mainly written in Python, so a Python environment will be requires, but no additional packages or libraries have to be downloaded. 
The input of what is to be transcribed has to be written in a *.txt*-file and the output will be a *.tex*-file, so to convert it to a *pdf*, any *LaTeX* program will be required, together with *tengwarscript* (https://ctan.org/pkg/tengwarscript). The fonts have to be also installed separately.

# Why Tengwriptor?
On the net there are a lot of guides and websites to write with Tengwar, but what I personally missed was the freedom, to control which mode to use (note that there are different writing modes) and to transcribe long texts (to practice reading for example) together with changing to any font and size of the text. Here *tengwarscript* was of course the solution I was looking for, but since using it is very amusing, I wrote this program with the goal to transcribe texts of any desired length, and then if needed some changes on the text could be made.

# Usage
<u>Input</u>: *.txt*-file
```
python3 text_transcriber.py [OPTIONS] file
```

<u>Output</u>: *.tex*-file with the transcribed text

<u>Options:</u>
- `-h`	show help menu
-  `-c`	autocompile
- `-f`	set font
- `-o`	give name to the output file (default name is that of input, interchanging ending by `.tex`)
- `-l`	chose language
- `-n`	chose number system (either decimal or duodecimal)
- `-d`	set dark style (black page with white letters)
- `-s`	quit spaces (for some scripts or title may be useful)
- `-p`	set paper size (in cm): paperwidth, paperheight, margin
- `-m`	center the whole text

<u>Accepted languages:</u> 
- Quenya

- Spanish

- Sindarin, Beleriand mode

  (default: Quenya)

*In the future*

- Sindarin (general mode)
- English

<u>Accepted fonts:</u> 

- Annatar

- Formal

- Noldor

- Quenya

- Sindarin

- Teleri

- Parmaite

- Elfica

- Gothika

  (default: annatar)

Variation of this fonts (like annataritalic or quenyacapI) are also accepted.
The fonts will have to be installed manually as explained in the *tengwarscript*-package.
