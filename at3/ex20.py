# 20. Escreva um programa para receber três notas. Depois calcule a média dessas notas e verifique se o estudante foi aprovado, reprovado ou está em recuperação.

from functions import ask_for_grade

grade1 = ask_for_grade("Insira a nota da primeira prova: ")
grade2 = ask_for_grade("Insira a nota da segunda prova: ")
grade3 = ask_for_grade("Insira a nota da terceira prova: ")
mean = (grade1 + grade2 + grade3) / 3

if mean >= 7:
    print("O aluno foi aprovado")
elif mean >= 4:
    print("O aluno está de recuperação")
else:
    print("O aluno foi reprovaado")