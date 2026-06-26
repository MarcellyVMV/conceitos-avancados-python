from pathlib import Path


# 1. Escreva uma função chamada largest, que lê o arquivo e retorna o maior número presente nele.
def largest() -> int:
    """
    Retorna o maior número presente em numbers.txt

    Returns:
        int: Maior número presente no arquivo.
    """
    file_path = Path(__file__).resolve().parent.parent / "assets" / "numbers.txt"
    with open(file_path, "r") as file:
        return max(int(line) for line in file)


if __name__ == "__main__":
    print(f"\nO maior número presente no arquivo é: {largest()}")
