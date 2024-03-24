# 29. Escreva um programa para ler números inteiros digitados pelo usuário, depois somar todos eles e exibir o resultado da soma. Para encerrar o programa utilize um valor negativo.

from functions import ask_for_int

partial = 0

while True:
    x = ask_for_int("Insira um inteiro: ")
    if x < 0:
        break
    partial += x

print(f"A soma dos números inseridos foi {partial}")