# 24. Escreva um programa que peça a altura (ex. 1.78) e o peso (80.5) do usuário e em seguida calcule o imc, informando também se está abaixo do peso, se está com peso normal, se está com sobrepeso, se está com obesidade ou se está com obesidade grave.

from functions import ask_for_float

while True:
    height = ask_for_float("Insira sua altura (em m): ")

    if height >= 0:
        break
    print("Insira uma altura válida")

while True:
    weight = ask_for_float("Insira seu peso (em kg): ")
    
    if weight > 0:
        break
    print("Insira um peso válido")

bmi = weight / height ** 2

print(f"Seu IMC é {bmi:.2f}kg/m²")

if bmi < 18.5:
    print("Você está abaixo do peso")
elif 18.5 <= bmi < 25:
    print("Seu peso está normal")
elif 25 <= bmi < 30:
    print("Você está acima do peso")
elif 30 <= bmi < 35:
    print("Você está obeso")
else:
    print("Você está severamente obeso")