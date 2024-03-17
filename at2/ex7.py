# 7. escreva um programa que solicita ao usuário a largura e o comprimento de um retângulo Calcule o perímetro e a área do retângulo, exibindo-os na tela

from functions import ask_for_float

print("Calculadora de perímetro e área de retângulo\n")

length = ask_for_float("Insira o comprimento do retângulo (em m): ")
width = ask_for_float("Insira a largura do retângulo (em m): ")

perimeter = length * 2 + width * 2
area = length * width

print(f"\nO perímetro do retângulo é {perimeter}m")
print(f"A área do retângulo é {area}m²")