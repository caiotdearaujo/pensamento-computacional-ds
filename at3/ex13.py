from functions import ask_for_int

x = ask_for_int("Insira um número: ")

if x % 2:
    print(f"{x} é ímpar")
else:
    print(f"{x} é par")