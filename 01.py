import math

class Square:
    def __init__(self, side_length):
        self.side_length = side_length

class Circle:
    def __init__(self, radius):
        self.radius = radius

class InscribedCircle(Square, Circle):
    def __init__(self, side_length):
        Square.__init__(self, side_length)
        # Радиус(radius) окружности равен половине длины стороны квадрата(square)
        self.radius = side_length / 2

    def area(self):
        return math.pi * (self.radius ** 2)

circle_in_square = InscribedCircle(19)
print(f"Радиус: {circle_in_square.radius} \nПлощадь: {circle_in_square.area():.2f}")
