from functions import ask_for_int

n1 = ask_for_int("Insira o primeiro inteiro: ")
n2 = ask_for_int("Insira o segundo inteiro: ")
n3 = ask_for_int("Insira o terceiro inteiro: ")

int_sum = sum((n1, n2, n3))

if int_sum > 0:
    print("A soma dos inteiros é positiva")
elif int_sum < 0:
    print("A soma dos inteiros é negativa")
else:
    print("A soma dos inteiros é igual a zero")