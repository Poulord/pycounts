from collections import Counter
from string import punctuation

#Ejercio 2 El Zen de Python
with open("zen.txt") as file:
    text = file.read()
    text = text.lower()
    for p in punctuation:
        text = text.replace(p, "")

#print(text)

words = text.split()
#print(words)
    
# Contador de palabras usando Counter
word_counts = Counter(words)
print (word_counts)