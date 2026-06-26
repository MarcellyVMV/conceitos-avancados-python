import statistics
import numpy as np


# 3. Pedir ao usuário uma matriz, validar a quantidade de elementos por linha, identificar linhas com tamanho diferente do mais comum e calcular o determinante da matriz usando numpy.linalg.det.
def receive_matrix() -> list[list[float]]:
    """
    Recebe do usuário uma matriz quadrada, linha por linha.
    O número de linhas solicitadas é determinado pela quantidade de elementos informada na primeira linha.

    Returns:
        list[list[float]]: Matriz informada pelo usuário.
    """
    matrix: list[list[float]] = []

    first_row = list(
        map(float, input(f"Digite a 1ª linha (Ex: [1, 2, 3]): ").split(","))
    )
    matrix.append(first_row)
    columns = len(first_row)

    i = 2
    while len(matrix) < columns:
        current_row = list(
            map(float, input(f"Digite a {i}ª linha (Ex: 1, 2, 3): ").split(","))
        )
        matrix.append(current_row)
        i += 1

    return matrix


def main() -> int:
    matrix = receive_matrix()

    row_lengths = [len(row) for row in matrix]
    expected_columns = statistics.mode(row_lengths)

    invalid_rows = [
        index + 1
        for index, length in enumerate(row_lengths)
        if length != expected_columns
    ]

    if invalid_rows:
        print("Erro: Linhas com número de elementos diferentes!")
        print(f"O número correto de elementos por linha é {expected_columns}.\n")
        print("Linhas com quantidade incorreta de elementos:")
        for row in invalid_rows:
            print(f"{row}ª linha = {matrix[row - 1]}")

        return 1

    determinant = np.linalg.det(matrix)
    print(f"O determinante é {determinant:.2f}")

    return 0


if __name__ == "__main__":
    raise SystemExit(main())
