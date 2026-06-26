class Point:
    """
    Representa um ponto em um plano cartesiano.

    Attributes:
        x (float): Coordenada x do ponto.
        y (float): Coordenada y do ponto.
    """

    def __init__(self, x: float, y: float) -> None:
        """
        Inicializa um ponto com coordenadas x e y.

        Args:
            x (float): Coordenada x do ponto.
            y (float): Coordenada y do ponto.
        """
        self.x = x
        self.y = y

    def __str__(self) -> str:
        """
        Retorna a representação textual do ponto.

        Returns:
            str: Representação do ponto no formato (x, y).
        """
        return f"({self.x}, {self.y})"


class Rectangle:
    """
    Representa um retângulo em um plano cartesiano.

    Attributes:
        center (Point): Centro do retângulo.
        width (float): Largura do retângulo.
        height (float): Altura do retângulo.
    """

    def __init__(self, center: Point, width: float, height: float) -> None:
        """
        Inicializa um retângulo com centro, largura e altura.

        Args:
            center (Point): Centro do retângulo.
            width (float): Largura do retângulo.
            height (float): Altura do retângulo.
        """
        self.center = center
        self.width = width
        self.height = height

    def rectangle_vertices(self) -> list[Point]:
        """
        Retorna os quatro vértices de um retângulo.

        Args:
            rectangle (Rectangle): Retângulo.

        Returns:
            list[Point]: Lista contendo os quatro vértices.
        """
        half_width = self.width / 2
        half_height = self.height / 2

        return [
            Point(self.center.x - half_width, self.center.y + half_height),
            Point(self.center.x + half_width, self.center.y + half_height),
            Point(self.center.x - half_width, self.center.y - half_height),
            Point(self.center.x + half_width, self.center.y - half_height),
        ]


# 2. Escreva uma classe chamada Circle com os atributos center e radius, onde center é um objeto do tipo Point e radius é um número.
class Circle:
    """
    Representa um círculo em um plano cartesiano.

    Attributes:
        center (Point): Centro do círculo.
        radius (float): Raio do círculo.
    """

    def __init__(self, center: Point, radius: float) -> None:
        """
        Inicializa um círculo com seu centro e raio.

        Args:
            center (Point): Centro do círculo.
            radius (float): Raio do círculo.
        """
        self.center = center
        self.radius = radius

    # 2.1 Escreva uma função chamada point_in_circle que receba um Circle e um Point e retorne True se o Point estiver dentro ou na borda do círculo.
    def point_in_circle(self, point: Point) -> bool:
        """
        Verifica se um ponto está dentro ou na borda do círculo.

        Args:
            point (Point): Ponto a ser analisado.

        Returns:
            bool: True se o ponto estiver dentro ou na borda do círculo, False caso contrário.
        """
        if (point.x - self.center.x) ** 2 + (
            point.y - self.center.y
        ) ** 2 <= self.radius**2:
            return True
        else:
            return False

    # 2.2 Escreva uma função chamada rect_in_circle que receba um Circle e um Rectangle e retorne True se o Rectangle estiver totalmente dentro ou na borda do círculo.
    def rect_in_circle(self, rectangle: Rectangle) -> bool:
        """
        Verifica se um retângulo está totalmente dentro ou na borda do círculo.

        Args:
            rectangle (Rectangle): Retângulo a ser analisado.

        Returns:
            bool: True se o retângulo estiver totalmente dentro ou na borda do círculo, False caso contrário.
        """
        vertices = Rectangle.rectangle_vertices(rectangle)

        for vertex in vertices:
            if not self.point_in_circle(vertex):
                return False
        return True

    # 2.3 Escreva uma função chamada rect_circle_overlap que receba um Circle e um Rectangle e retorne True se qualquer um dos cantos do Rectangle estiver dentro do círculo.
    def verticesRect_circle_overlap(self, rectangle: Rectangle) -> bool:
        """
        Verifica se um dos vertices de um retângulo está dentro ou na borda do círculo.

        Args:
            rectangle (Rectangle): Retângulo a ser analisado.

        Returns:
            bool: True se algum dos vertices do retângulo estiver dentro ou na borda do círculo, False caso contrário.
        """
        vertices = Rectangle.rectangle_vertices(rectangle)
        for vertex in vertices:
            if self.point_in_circle(vertex):
                return True
        return False

    # 2.3 Ou, para uma versão mais desafiadora, retorne True se qualquer parte do Rectangle estiver dentro do círculo.
    def rect_circle_overlap(self, rectangle: Rectangle) -> bool:
        """
        Verifica se qualquer parte de um retângulo está dentro ou na borda do círculo.

        Args:
            rectangle (Rectangle): Retângulo a ser analisado.

        Returns:
            bool: True se qualquer parte do retângulo estiver dentro ou na borda do círculo, False caso contrário.
        """
        for x in range(
            int(rectangle.center.x - rectangle.width / 2),
            int(rectangle.center.x + rectangle.width / 2),
        ):
            for y in range(
                int(rectangle.center.y - rectangle.height / 2),
                int(rectangle.center.y + rectangle.height / 2),
            ):
                point = Point(x, y)
                if self.point_in_circle(point):
                    return True
        return False


if __name__ == "__main__":
    # Exemplo
    circle1 = Circle(Point(150, 100), 75)
    point1 = Point(100, 100)

    print(circle1.point_in_circle(point1))  # Output: True

    rectangle1 = Rectangle(Point(100, 100), 100, 50)
    rectangle2 = Rectangle(Point(150, 100), 200, 250)

    print(circle1.rect_in_circle(rectangle1))  # Output: False
    print(circle1.verticesRect_circle_overlap(rectangle1))  # Output: True
    print(circle1.rect_circle_overlap(rectangle2))  # Output: True
