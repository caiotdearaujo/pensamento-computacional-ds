# 31. Escreva um programa que leia duas palavras digitadas pelo usuário. Depois o programa vai concatenar essas duas palavras e apresentá-las.

word1 = input("Insira uma palavra: ").strip()
word2 = input("Insira outra palavra: ").strip()

concat_word = word1 + word2

print(f"Se concatenarmos ambas as palavras o resultado será: {concat_word}")