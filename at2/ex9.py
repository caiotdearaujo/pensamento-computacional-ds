# 9. Escreva um programa que solicita ao usuário o valor do raio de uma esfera. Calcule o volume da esfera utilizando a fórmula V = (4/3) * pi * raio³

from functions import ask_for_float
from math import pi

print("Calculadora de volume de esfera\n")

radius = ask_for_float("Insira o raio da esfera (em m): ")

volume = (4/3) * pi * radius

print(f"\nO volume da esfera é {volume}m³")