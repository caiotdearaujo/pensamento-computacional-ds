# 6.Escreva um programa que solicita ao usuário o raio do círculo e calcule essa área usando a fórmula A = π * raio²

from functions import ask_for_float
from math import pi

print("Calculadora de área de círculo\n")

radius = ask_for_float("Insira o raio do círculo (em m): ")

area = pi * radius ** 2

print(f"\nA área do círculo é {area}m²")