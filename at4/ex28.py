# 28. Escreva um programa que imprima uma sequência de números (0 até 100, por exemplo).

from functions import ask_for_int

start = ask_for_int("Insira o início do intervalo: ")
stop = ask_for_int("Insira o fim do intervalo: ") + 1

interval = (i for i in range(start, stop))
print(*interval)