# 26. Escreva um programa que leia dois números inteiros e verifica se o primeiro número é divisível pelo segundo.

from functions import ask_for_int

x = ask_for_int("Insira um inteiro: ")
y = ask_for_int("Insira outro inteiro: ")

try:
    if x % y:
        print(f"{x} não é divisível por {y}")
    else:
        print(f"{x} é divisível por {y}")
except ZeroDivisionError:
    print("Não é possivel dividir por 0")