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