#!/usr/bin/venv python3
#
# Takes the text file and then splits the text into the words, such that we can transcribe them
# For every paragraph a different list will be used
import re

def splitter(file):
    """
    Takes the text of 'file' and gives a list of lists (paragraphs), where the words are splitted
    """

    paragraph_lists = []

    with open(file, "r", encoding="utf-8") as f:
        text = f.read()

    # split paragraphs; through blank lines
    paragraphs = re.split(r'\n\s*\n', text.strip())

    # split into words or single punctuation characters
    token_pattern = r"\w+|[^\w\s]"

    for paragraph in paragraphs:
        tokens = re.findall(token_pattern, paragraph)
        paragraph_lists.append(tokens)

    return paragraph_lists
