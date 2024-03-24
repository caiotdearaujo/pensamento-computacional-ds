# 30. Escreva um programa simples para calcular a quantidade de vogais em uma frase digitada pelo usuário.

from unicodedata import normalize

vowels = ('a', 'e', 'i', 'o', 'u')

sentence = input("Insira uma frase: ").lower()
sentence = normalize('NFKD', sentence).encode('ASCII','ignore').decode('ASCII')

n = 0
for i in sentence:
    if i in vowels:
        n += 1

if n == 1:
    print(f"A frase inserida tem 1 vogal")
else:
    print(f"A frase inserida tem {n} vogais")