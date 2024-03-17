# 8. Escreva um programa que solicita ao usuário a massa do objeto e velocidade. Calcule a energia cinética usando a fórmula E = (mv²) / 2

from functions import ask_for_float

print("Calculadora de energia cinética\n")

mass = ask_for_float("Insira a massa do corpo (em kg): ")
velocity = ask_for_float("Insira a velocidade do corpo (em m/s): ")

kinetic_energy = (mass * velocity ** 2) / 2

print(f"\nA enegia cinética do corpo é {kinetic_energy}J")