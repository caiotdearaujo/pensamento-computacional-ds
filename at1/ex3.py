# 3. Crie um programa que calcule e exiba a média aritmética de três notas informadas pelo usuário.

from functions import ask_for_float

print("Média aritmética de três notas \n")

n1 = ask_for_float("Insira a primeira nota: ")
n2 = ask_for_float("Insira a segunda nota: ")
n3 = ask_for_float("Insira a terceira nota: ")

mean = (n1+n2+n3)/3

print(f"A média entre as notas informadas é: {mean}")