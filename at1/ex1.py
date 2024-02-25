from functions import ask_for_float

print("Operações aritméticas básicas entre números \n")

n1 = ask_for_float("Insira um número: ")
n2 = ask_for_float("Insira outro número: ")

sum = n1 + n2
subtraction = n1 - n2
multiplication = n1 * n2
division = n1 / n2

print()

print(f"A soma entre os números é: {sum}")

print(f"A subtração entre os números é: {subtraction}")

print(f"A multiplicação entre os números é: {multiplication}")

if n2 != 0:
    print(f"A divisão entre os números é: {division}")
else:
    print("Não é possível dividir por zero")