text = input('Digite a primeira linha de uma canção preferida: ')

start_number = int(input('Número inicial: '))
end_number = int(input('Número final: '))

print(f"O tamanho da canção é {len(text)} caracteres.")
print(f"O trecho da canção é: {text[start_number:end_number]}")