# 25. Escreva um programa que leia a idade do usuário e apresente uma mensagem, informando se o usuário é uma criança, adolescente, adulto ou idoso.

from functions import ask_for_int

while True:
    age = ask_for_int("Insira sua idade: ")
    
    if age >= 0:
        break
    print("Como assim você não nasceu? Insira uma idade válida")

if age < 13:
    print("Você é uma criança")
elif 13 <= age < 18:
    print("Você é um adolescente")
elif 18 <= age < 60:
    print("Você é um adulto")
else:
    print("Você é um idoso")