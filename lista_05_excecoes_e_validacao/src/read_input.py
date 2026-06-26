# 2. Escreva uma função chamada read_input, que solicita ao usuário uma entrada até que ele digite um número inteiro que esteja dentro dos limites fornecidos. A função retorna o valor inteiro válido.
def read_input(n1: int, n2: int) -> int:
    """
    Solicita ao usuário um número inteiro dentro do intervalo [n1, n2].
    Repete até que a entrada seja válida.

    Args:
        n1 (int): limite inferior.
        n2 (int): limite superior.

    Returns:
        int: número inteiro válido
    """
    while True:
        try:
            number = int(input(f"\nPor favor entre com um número: "))

        except ValueError:
            print(f"Você deve entrar com um número inteiro.")
            continue

        if n1 <= number <= n2:
            return number

        print(f"Você deve entrar com um número inteiro entre {n1} e {n2}.")


if __name__ == "__main__":
    print(f"Você digitou {read_input(5, 10)}")
