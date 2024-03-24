# 23. Escreva um programa que leia o dia da semana e apresente uma mensagem informando se é um dia útil, se é um dia de fim de semana ou se é dia inválido.

week = ('segunda', 'terça', 'quarta', 'quinta', 'sexta')
weekend = ('sábado', 'domingo')

while True:
    day = input("Que dia da semana é hoje? ").lower().strip()

    if day in week:
        print("Hoje é um dia útil")
        break
    if day in weekend:
        print("Hoje é um dia de fim de semana")
        break
    print("Insira um dia válido")