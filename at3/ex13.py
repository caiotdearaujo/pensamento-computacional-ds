# 13. Escreva um programa para verificar se um número é par ou ímpar.

from functions import ask_for_int

x = ask_for_int("Insira um número: ")

if x % 2:
    print(f"{x} é ímpar")
else:
    print(f"{x} é par")