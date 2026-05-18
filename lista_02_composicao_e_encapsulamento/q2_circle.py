class Circle:
    #Função inicial
    def __init__(self, center, radius) -> None:
        self.center = center
        self.radius = radius

    #Função para conferir se um ponto está dentro do circulo
    def point_in_circle(self, point):
        if (point.x - self.center.x)**2 + (point.y - self.center.y)**2 <= self.radius**2:
            return True
        else:
            return False

    #Função para conferir se um retángulo totalmente está dentro do circulo
    def rect_in_circle(self, rectangle):
        if ((rectangle.center.x - rectangle.width / 2) - self.center.x)**2 + ((rectangle.center.y + rectangle.height / 2) - self.center.y)**2 <= self.radius**2 \
        and ((rectangle.center.x + rectangle.width / 2) - self.center.x)**2 + ((rectangle.center.y + rectangle.height / 2) - self.center.y)**2 <= self.radius**2 \
        and ((rectangle.center.x - rectangle.width / 2) - self.center.x)**2 + ((rectangle.center.y - rectangle.height / 2) - self.center.y)**2 <= self.radius**2 \
        and ((rectangle.center.x + rectangle.width / 2) - self.center.x)**2 + ((rectangle.center.y - rectangle.height / 2) - self.center.y)**2 <= self.radius**2:
            return True
        else:
            return False

    #Função para conferir se um retángulo está dentro do circulo
    def rect_circle_overlap(self, rectangle):
        if ((rectangle.center.x - rectangle.width / 2) - self.center.x)**2 + ((rectangle.center.y + rectangle.height / 2) - self.center.y)**2 <= self.radius**2 \
        or ((rectangle.center.x + rectangle.width / 2) - self.center.x)**2 + ((rectangle.center.y + rectangle.height / 2) - self.center.y)**2 <= self.radius**2 \
        or ((rectangle.center.x - rectangle.width / 2) - self.center.x)**2 + ((rectangle.center.y - rectangle.height / 2) - self.center.y)**2 <= self.radius**2 \
        or ((rectangle.center.x + rectangle.width / 2) - self.center.x)**2 + ((rectangle.center.y - rectangle.height / 2) - self.center.y)**2 <= self.radius**2:
            return True
        else:
            return False

    #Função para conferir se qualquer parte do retángulo está dentro do circulo
    def rect_circle_overlap2(self, rectangle):
        for x in range(int(rectangle.center.x - rectangle.width / 2), int(rectangle.center.x + rectangle.width / 2)):
            for y in range(int(rectangle.center.y - rectangle.height / 2), int(rectangle.center.y + rectangle.height / 2)):
                if (x - self.center.x)**2 + (y - self.center.y)**2 <= self.radius**2:
                    return True
        else:
            return False

class Rectangle:
    #Função inicial
    def __init__(self, center, width, height):
        self.center = center
        self.width = width
        self.height = height

class Point:
    #Função inicial
    def __init__(self, x, y):
        self.x = 0
        self.y = 0

# Exemplo
circle1 = Circle(Point(150, 100), 75)
point1 = Point(100, 100)

print(circle1.point_in_circle(point1))

rectangle1 = Rectangle(Point(100, 100), 100, 50)
rectangle2 = Rectangle(Point(150, 100), 200, 250)

print(circle1.rect_in_circle(rectangle1))
print(circle1.rect_circle_overlap(rectangle1))
print(circle1.rect_circle_overlap2(rectangle2))