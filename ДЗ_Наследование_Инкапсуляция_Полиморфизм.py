import math
from abc import ABC, abstractmethod


class Shape(ABC):
    @abstractmethod
    def area(self):
        pass


class Rectangle(Shape):
    def __init__(self, length, width):
        self.length = length
        self.width = width

    def area(self):
        return self.length * self.width


class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius

    def area(self):
        return math.pi * math.pow(self.radius, 2)


rect = Rectangle(5, 4)
circ = Circle(7)
print(f"Площадь прямоугольника со сторонами {rect.length} и {rect.width} = {rect.area()}")
print(f"Площадь круга с радиусом {circ.radius} = {circ.area():.2f}")