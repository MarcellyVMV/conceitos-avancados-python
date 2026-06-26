import numpy as np
from scipy import linalg as la

# 2. Encontre as tensões VA, VB e VC.
if __name__ == "__main__":
    matrix_a = np.array(
        [
            [57, -4, -30],
            [28, -123, 60],
            [140, 40, -243],
        ]
    )

    vector_b = np.array([500, 0, 840])

    voltages = la.solve(matrix_a, vector_b)

    va, vb, vc = np.round(voltages, 2)

    print(f"Tensão VA: {va:.2f}\n" f"Tensão VB: {vb:.2f}\n" f"Tensão VC: {vc:.2f}\n")
