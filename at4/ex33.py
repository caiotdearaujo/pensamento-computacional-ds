# 33. Escreva um programa que leia uma frase digitada pelo usuário, depois troque a ocorrência da letra “a” pela letra “e” e depois apresente a frase nova.

from unicodedata import normalize

sentence = input("Insira uma frase: ").strip()
new_sentence = ''

for i in sentence:
    j = normalize('NFKD', i).encode('ASCII','ignore').decode('ASCII')
    if j == 'a':
        new_sentence += 'e'
    elif j == 'A':
        new_sentence += 'E'
    else:
        new_sentence += i

print("A frase depois de trocarmos todos os a's por e's ficou:", new_sentence)