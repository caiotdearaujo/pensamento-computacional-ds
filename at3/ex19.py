# 19. Escreva um programa para receber a data de nascimento do usuário. Calcule a idade atual e verifique se o usuário está apto a votar.

import datetime

def ask_for_date(message: str) -> datetime.date:
    while True:
        try: 
            date_entry = input(message + " (no formato DD/MM/YYYY): ").strip()
            day, month, year = map(int, date_entry.split('/'))
            return datetime.date(year, month, day)
        except ValueError:
            print("Insira uma data válida\n")

today = datetime.date.today()

while True:
    birthday = ask_for_date("Insira sua data de aniversário") 
    age = (today - birthday) // datetime.timedelta(days=365.2425)

    if age >= 0:
        break
    print("Insira uma data de nascimento válida\n")

print(f"O usuário tem {age} anos", end=' ')

if age >= 16:
    print("e está apto a votar")
else:
    print("e não está apto a votar")