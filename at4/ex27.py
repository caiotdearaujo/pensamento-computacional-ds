# 27. Escreva um programa que apresente uma sequência de números (1 até 10, por exemplo). Para isso, utilize a instrução while e instrução for.

from functions import ask_for_int

start = ask_for_int("Insira o início do intervalo: ")
stop = ask_for_int("Insira o fim do intervalo: ") + 1

for i in range(start, stop):
    print(i, end=' ')