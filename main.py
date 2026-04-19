import os


def TextProcessor(path_file):
    txt = []
    with open(path_file, "r", encoding="utf-8") as f:
        for line in f:
            line = line.lower().strip()
            if(line != ""):
                txt.append(line)
    return txt    


path = os.getcwd()
text = TextProcessor(path + "/meu_novo_mundo.txt")

print(text)
    