from functions import ask_for_grade

grade1 = ask_for_grade("Insira a nota da primeira prova: ")
grade2 = ask_for_grade("Insira a nota da segunda prova: ")
min_grade = ask_for_grade("Insira a nota de média da escola: ")

if grade1 >= min_grade:
    print("O estudante foi aprovado na prova 1")
else:
    print("O estudante foi reprovado na prova 1")

if grade2 >= min_grade:
    print("O estudante foi aprovado na prova 2")
else:
    print("O estudante foi reprovado na prova 2")