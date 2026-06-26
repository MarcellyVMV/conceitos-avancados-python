import numpy as np
from scipy import linalg as la

# 3. Determinar a quantidade de trabalhadores dos tipos A, B e C necessária para atender às horas exigidas em cada turno, formulando e resolvendo um sistema de equações lineares.
if __name__ == "__main__":
    matrix_a = np.array(
        [
            [3, 1, 1],
            [1, 3, 1],
            [1, 1, 3],
        ]
    )

    vector_b = np.array([30, 40, 20])

    workers = la.solve(matrix_a, vector_b)

    worker_a, worker_b, worker_c = np.round(workers, 2)

    print(
        f"Trabalhadores do tipo A = {worker_a:.2f}\n"
        f"Trabalhadores do tipo B = {worker_b:.2f}\n"
        f"Trabalhadores do tipo C = {worker_c:.2f}\n"
    )
