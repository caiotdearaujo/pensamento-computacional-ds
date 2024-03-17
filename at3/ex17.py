from functions import ask_for_int

n1 = ask_for_int("Insira o primeiro inteiro: ")
n2 = ask_for_int("Insira o segundo inteiro: ")
n3 = ask_for_int("Insira o terceiro inteiro: ")

int_sum = sum((n1, n2, n3))

if not int_sum % 5:
    print("A soma dos inteiros é divisível por 5")
else:
    print("A soma dos inteiros não é divisível por 5")