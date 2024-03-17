# 16. Escreva um programa que receba duas notas (uma nota para a prova1 e a outra para a prova2). Depois calcule a média aritmética simples dessas notas e verifique se o estudante é aprovado ou reprovado.

from functions import ask_for_grade

grade1 = ask_for_grade("Insira a nota da primeira prova: ")
grade2 = ask_for_grade("Insira a nota da segunda prova: ")
min_grade = ask_for_grade("Insira a nota de média da escola: ")
mean = (grade1 + grade2) / 2

if mean >= min_grade:
    print(f"O aluno foi aprovado, pois sua média foi {mean}")
else:
    print(f"O aluno foi reprovado, pois sua média foi {mean}")