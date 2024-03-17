from functions import ask_for_float

x = ask_for_float("Insira um número: ")

if x > 0:
    print("O número é positivo")
elif x < 0:
    print("O número é negativo")
else:
    print("O número é zero")