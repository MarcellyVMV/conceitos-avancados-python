import statistics
import numpy as np


def receive_matrix() -> list[list[float]]:
    """
    Recebe uma matriz quadrada do usuário.
    O número de linhas e de colunas é determinado pela quantidade de elementos informada na primeira linha.

    Returns:
        list[list[float]]: Matriz informada pelo usuário.
    """
    matrix: list[list[float]] = []

    first_row = list(
        map(float, input(f"Digite a 1ª linha (Ex: [1, 2, 3]): ").split(","))
    )
    matrix.append(first_row)
    columns = len(first_row)

    for i in range(2, columns + 1):
        while True:
            current_row = list(
                map(float, input(f"Digite a {i}ª linha (Ex: 1, 2, 3): ").split(","))
            )
            if len(current_row) == columns:
                matrix.append(current_row)
                break
            print(f"Erro: a {i}ª linha deve possuir {columns} elementos.")

    return matrix


def main() -> int:
    matrix = receive_matrix()

    determinant = np.linalg.det(matrix)
    print(f"O determinante é {determinant:.2f}")

    return 0


if __name__ == "__main__":
    raise SystemExit(main())
