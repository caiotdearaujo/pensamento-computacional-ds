# 32. Escreva um programa que leia uma palavra digitada pelo usuário e depois apresente cada letra separadamente

word = input("Insira uma palavra: ").strip()

for i, j in enumerate(word):
    print(f"Letra {i+1}: {j}")