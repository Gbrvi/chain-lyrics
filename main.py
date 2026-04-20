import os
import re
from unidecode import unidecode
import random
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


def MarkovChain(cleaned_text, n_gram=2):
    markov_model = {}
    for i in range(len(cleaned_text) - n_gram):
        current_state = tuple(cleaned_text[i: i+ n_gram])
        
        next_state = cleaned_text[i + n_gram]
        
        if current_state not in markov_model:
            markov_model[current_state] = {}
            markov_model[current_state][next_state] = 1
        else:
            if next_state in markov_model[current_state]:
                markov_model[current_state][next_state] += 1
            else:
                markov_model[current_state][next_state] = 1
            
    for curr_state, transition in markov_model.items():
        total = sum(transition.values())
        for state, count in transition.items():
            markov_model[curr_state][state] = count/total
            
    return markov_model
        
        
def generate_lyrics(markov_model, limit=100, start=None):
    n = 0
    if(start == None):
        start = random.choice(list(markov_model.keys()))
        
    current_state = start

    
    song_words = list(current_state)
    
    while n < limit:
        next_word = random.choices(list(markov_model[current_state].keys()),
                                    list(markov_model[current_state].values()))[0]
        
        song_words.append(next_word)
        
        current_state = current_state[1:] + (next_word, )

        n += 1
        
    return " ".join(song_words)
    
    
                
                
path = os.getcwd()
text = TextProcessor(path + "/meu_novo_mundo.txt")

clean = CleanedText(text)

markov = MarkovChain(clean)
    
for i in range(5):
    print(generate_lyrics(markov, 20))
    print("\n")

