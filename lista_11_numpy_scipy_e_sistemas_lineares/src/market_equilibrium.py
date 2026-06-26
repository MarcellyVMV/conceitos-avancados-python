import numpy as np
from scipy import linalg as la

# 1. Determinar os preços de equilíbrio de quatro produtos igualando oferta e demanda, formular o sistema na forma matricial Ax=b, resolver o sistema e exibir os preços de equilíbrio de cada produto.
if __name__ == "__main__":
    matrix_a = np.array(
        [
            [7, 3, 1.5, 0],
            [2, 7, 0, 2],
            [1.5, 2, 4.5, 0],
            [0, 2, 2.5, 8],
        ]
    )

    vector_b = np.array([80, 60, 85, 90])

    prices = la.solve(matrix_a, vector_b)

    pa, pb, pc, pd = np.round(prices, 2)

    print(
        f"Produto A: {pa:.2f}\n"
        f"Produto B: {pb:.2f}\n"
        f"Produto C: {pc:.2f}\n"
        f"Produto D: {pd:.2f}\n"
    )
