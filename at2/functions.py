def ask_for_float(message: str) -> float:
    while True:
        try:
            return float(input(message))
        except ValueError:
            print("Insira um número\n")