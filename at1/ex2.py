# 2. Escreva um programa que calcule a média aritmética de dois números.

from functions import ask_for_float

print("Média aritmética de dois números \n")

n1 = ask_for_float("Insira um número: ")
n2 = ask_for_float("Insira outro numero: ")

mean = (n1+n2)/2

print(f"A média dos números é: {mean}")