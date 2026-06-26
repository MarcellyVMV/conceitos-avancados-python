from pathlib import Path


# 2. Escreva uma função que leia um arquivo e exiba o número de linhas de código nesse arquivo, excluindo comentários e linhas em branco. Faça tratamento de erros caso o arquivo não exista.
def lines(file: str) -> int:
    """
    Retorna o número de linhas de código de um arquivo.

    Args:
        file (str): Caminho do arquivo.

    Returns:
        int: Número de linhas de código do arquivo.
    """
    count = 0
    with open(file, "r") as file:
        for line in file:
            line = line.strip()
            # Ignora linhas vazias e linhas que começam com "#" (comentários).
            if line and not line.startswith("#"):
                count += 1
        return count


if __name__ == "__main__":
    try:
        file = input("Digite o caminho do arquivo: ")
        file_path = Path(file).expanduser().resolve()

        print(f"\nO arquivo possui {lines(file_path)} linhas.")
    except FileNotFoundError:
        print(f"\nO arquivo '{file_path}' não foi encontrado.")
