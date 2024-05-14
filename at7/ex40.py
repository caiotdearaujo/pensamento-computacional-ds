name = input("Insira seu nome: ").strip()
print(f"Seu nome tem {len(name)} caracteres.")

surname = input("Insira seu sobrenome: ").strip()
print(f"Seu sobrenome tem {len(surname)} caracteres.")

full_name = name + " " + surname
full_name = full_name.title()
print(f"Seu nome completo é {full_name} e tem {len(full_name)} caracteres.")