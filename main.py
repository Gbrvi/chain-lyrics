import os
import re
from unidecode import unidecode
def TextProcessor(path_file):
    txt = []
    with open(path_file, "r", encoding="utf-8") as f:
        for line in f:
            line = line.lower().strip()
            if(line != ""):
                txt.append(unidecode(line))
    return txt    


def CleanedText(text):
    cleaned_text = []
    word_count = 0
    for line in text:
        if line != "":
            words = re.findall(r'\b\w+\b', line)
            cleaned_text.extend(words)
    return cleaned_text
                
                
path = os.getcwd()
text = TextProcessor(path + "/meu_novo_mundo.txt")

clean = CleanedText(text)


print(clean)
    