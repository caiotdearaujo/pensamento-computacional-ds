def ask_for_float(message: str) -> float:
    while True:
        try:
            return float(input(message))
        except ValueError:
            print("Insira um número\n")


def ask_for_int(message: str) -> int:
    while True:
        try:
            return int(input(message))
        except ValueError:
            print("Insira um inteiro\n")


def ask_for_grade(message: str) -> float:
    while True:
        grade = ask_for_float(message)

        if 0 <= grade <= 10:
            return grade
        print("Insira uma nota no intervalo de 0 a 10")