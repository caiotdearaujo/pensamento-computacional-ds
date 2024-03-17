# 12. Escreva um programa que solicita três números e verifique qual deles é o maior.

from functions import ask_for_float

n1 = ask_for_float("Insira o primeiro número: ")
n2 = ask_for_float("Insira o segundo número: ")
n3 = ask_for_float("Insira o terceiro número: ")

numbers = n1, n2, n3

print(f"O maior número é {max(numbers)}")