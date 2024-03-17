# 5. Escreva um programa que calcule o IMC de um indivíduo, utilizando a fórmula IMC = peso / altura².

from functions import ask_for_float

print("Calculadora de índice de massa corporal \n")

height = ask_for_float("Insira sua altura (em cm): ")
height /= 100
weight = ask_for_float("Insira seu peso (em kg): ")

imc = weight/height**2

print(f"Seu IMC é igual a: {imc:.2f}")