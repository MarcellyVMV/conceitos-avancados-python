# 3. Solicite uma fração X/Y, valide a entrada (inteiros, Y≠0 e X≤Y), e exibe, como uma porcentagem arredondada ou “E”,se restar 1% ou menos, ou “F”, se restar 99% ou mais.
def fuel_gauge() -> str:
    """
    Solicita ao usuário uma fração e retorna a porcentagem de combustível restante.

    Returns:
        str: Combustível restante em porcentagem.
    """
    while True:
        try:
            x, y = map(int, input("\nFração: ").split("/"))
            if y <= 0:
                raise ZeroDivisionError("Y não pode ser zero ou negativo")
            if x > y or x < 0:
                raise ValueError("X não pode ser maior que Y ou negativo")
        except (ZeroDivisionError, ValueError) as e:
            print(f"Erro: {e}. Tente novamente.")
            continue
        else:
            percentage = round((x / y) * 100)
            if percentage <= 1:
                return "E"
            elif percentage >= 99:
                return "F"
            else:
                return f"{percentage}%"


if __name__ == "__main__":
    print(fuel_gauge())
