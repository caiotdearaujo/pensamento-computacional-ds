name = input("Insira seu nome: ").strip()

if len(name) < 5:
    surname = input("Insira seu sobrenome: ").lower()
    print(name.upper()+surname.upper())
else:
    print(name.lower())