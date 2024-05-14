password1 = input("Insira a senha: ")
password2 = input("Confirme a senha: ")

if password1 == password2:
    print("Autorizado")
elif (password1.isupper() and password2.islower()) or (password1.islower() and password2.isupper()):
    print("As senhas devem ser iguais.")
else:
    print("As senhas não são iguais.")