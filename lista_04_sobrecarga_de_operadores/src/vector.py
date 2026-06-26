from __future__ import annotations
from math import sqrt


# 1.Crie uma classe chamada Vector que represente vetores no espaço bidimensional e implemente os operadores de adição (+), subtração (-), multiplicação por escalar (*) e produto escalar (*). E um método que calcule a magnitude do vetor.
class Vector:
    """
    Representa um vetor bidimensional com coordenadas x e y.
    Suporta operações de adição, subtração, multiplicação por escalar, produto escalar e cálculo da magnitude.

    Attributes:
        x (float): Componente x do vetor.
        y (float): Componente y do vetor.
    """

    def __init__(self, x: float, y: float) -> None:
        """
        Inicializa um novo vetor com as coordenadas x e y.

        Args:
            x (float): Componente x do vetor.
            y (float): Componente y do vetor.
        """
        self.x = x
        self.y = y

    def __str__(self) -> str:
        """
        Retorna a representação do vetor no formato (x, y).

        Returns:
            str: String representando o vetor no formato (x, y).
        """
        return f"({self.x}, {self.y})"

    def __repr__(self) -> str:
        """
        Retorna a representação oficial do vetor, útil para depuração.

        Returns:
            str: String representando o vetor no formato Vector(x, y).
        """
        return f"Vector({self.x}, {self.y})"

    def __add__(self, other: Vector) -> Vector:
        """
        Soma dois vetores, retornando um novo vetor resultante da soma.

        Args:
            other (Vector): Vetor a ser somado com o vetor atual.

        Returns:
            Vector: Vetor resultante da soma dos dois vetores.
        """
        if not isinstance(other, Vector):
            return NotImplemented
        return Vector(self.x + other.x, self.y + other.y)

    def __sub__(self, other: Vector) -> Vector:
        """
        Subtrai dois vetores, retornando um novo vetor resultante da subtração.

        Args:
            other (Vector): Vetor a ser subtraído do vetor atual.

        Returns:
            Vector: Vetor resultante da subtração dos dois vetores.
        """
        if not isinstance(other, Vector):
            return NotImplemented
        return Vector(self.x - other.x, self.y - other.y)

    def __mul__(self, other: Vector | float) -> Vector | float:
        """
        Multiplica o vetor por um escalar ou calcula o produto escalar com outro vetor.

        Args:
            other (Vector or float): Se for um vetor, calcula o produto escalar. Se for um número, multiplica o vetor por esse escalar.

        Returns:
            Vector | float: Retorna um novo vetor se other for um escalar, ou o produto escalar se other for outro vetor.
        """
        if isinstance(other, Vector):
            return self.x * other.x + self.y * other.y
        elif isinstance(other, (int, float)):
            return Vector(self.x * other, self.y * other)
        return NotImplemented

    def __rmul__(self, scalar: float) -> Vector:
        """
        Permite a multiplicação por escalar com o escalar à esquerda.

        Args:
            scalar (float): Escalar a ser multiplicado pelo vetor.

        Returns:
            Vector: Novo vetor resultante da multiplicação por escalar.
        """
        if not isinstance(scalar, (int, float)):
            return NotImplemented
        return Vector(self.x * scalar, self.y * scalar)

    def magnitude(self) -> float:
        """
        Calcula o módulo do vetor usando a fórmula da raiz quadrada da soma dos quadrados das componentes.

        Returns:
            float: Módulo do vetor.
        """
        return sqrt(self.x**2 + self.y**2)


if __name__ == "__main__":
    # Exemplo
    v1 = Vector(3, 4)
    v2 = Vector(1, 2)

    print(f"\nSoma: {v1 + v2}")  # Output: (4, 6)
    print(f"Subtração: {v1 - v2}")  # Output: (2, 2)
    print(f"Multiplicação por escalar: {v1 * 3}")  # Output: (9, 12)
    print(f"Produto Escalar: {v1 * v2}")  # Output: 11
    print(f"Magnitude de v1: {v1.magnitude()}\n")  # Output: 5.0
