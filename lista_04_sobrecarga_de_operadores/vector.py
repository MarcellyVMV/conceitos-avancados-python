from math import sqrt
class Vector:
    #Construtor
    def __init__(self, x, y):
        self.x = x
        self.y = y

    #Método para imprimir o vetor
    def __str__(self):
        return f"({self.x}, {self.y})"

    #Método para somar o vetor
    def __add__(self, other):
        return Vector(self.x + other.x, self.y + other.y)

    #Método para subtrair o vetor
    def __sub__(self, other):
        return Vector(self.x - other.x, self.y - other.y)

    #Método para multiplicar o vetor
    def __mul__(self, other):
        if isinstance(other, Vector):
            return self.x * other.x + self.y * other.y
        else:
            return Vector(self.x * other, self.y * other)

    #Método que retorna o módulo do vetor
    def magnitude(self):
        return sqrt(self.x ** 2 + self.y ** 2)

#Exemplo
v1 = Vector(3, 4)
v2 = Vector(1, 2)

print(f"\nSoma: {v1 + v2}") # Output: (4, 6)
print(f"Subtração: {v1 - v2}") # Output: (2, 2)
print(f"Multiplicação por escalar: {v1 * 3}") # Output: (9, 12)
print(f"Produto Escalar: {v1 * v2}") # Output: 11
print(f"Magnitude de v1: {v1.magnitude()}\n") # Output: 5.0