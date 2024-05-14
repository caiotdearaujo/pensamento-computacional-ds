word = input("Insira uma palavra em letras maiúsculas: ")

while word.islower():
    print("A palavra não está em letras maiúsculas.")
    word = input("Insira uma palavra em letras maiúsculas: ")

print(f"A palavra é {word}")