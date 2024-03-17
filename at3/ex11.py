# 11. Escreva um programa para verificar se o primeiro número ou o segundo número é maior, caso contrário eles são iguais.

from functions import ask_for_float

n1 = ask_for_float("Insira o primeiro número: ")
n2 = ask_for_float("Insira o segundo número: ")

if n1 > n2:
    print("O primeiro número é maior que o segundo")
elif n1 < n2:
    print("O segundo número é maior que o primeiro")
else:
    print("Os números são iguais")