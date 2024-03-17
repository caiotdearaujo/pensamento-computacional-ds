# 10. Escreva um programa para testar se idade é maior ou menor do que 18 anos.

def ask_for_age(message: str) -> int:
    while True:
        try:
            age = int(input(message))
        except ValueError:
            print("Insira um número\n")
            continue
        
        if age >= 0:
            return age
        print("Insira uma idade válida\n")


def check_age(age: int):
    if age > 18:
        print("Você tem mais de 18 anos")
        return
    if age == 18:
        print("Você tem 18 anos")
        return
    print("Você é menor de 18 anos")


print("Checagem de idade\n")

age = ask_for_age("Insira sua idade: ")

check_age(age)