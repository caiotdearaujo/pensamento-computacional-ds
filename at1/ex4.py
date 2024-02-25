import math
from functions import ask_for_float

print("Média geométrica de três números \n")

n1 = ask_for_float("Insira o primeiro número: ")
n2 = ask_for_float("Insira o segundo número: ")
n3 = ask_for_float("Insira o terceiro número: ")

geometric_mean = math.sqrt(n1*n2*n3)

print(f"A média geométrica entre os números é: {geometric_mean}")