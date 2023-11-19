"""
Завдання 2
Для класів із першого завдання перевизначте магічні
методи int (повертає площу) та str (повертає інформацію
про фігуру).
"""
import math
from abc import ABC, abstractmethod

class Figure(ABC):
    @abstractmethod
    def area(self):
        pass

    def __str__(self):
        return f"Figure: {type(self).__name__}"

    def __int__(self):
        return int(self.area())

class Rectangle(Figure):
    def __init__(self, length, width):
        self.length = length
        self.width = width

    def area(self):
        return self.length * self.width

class Circle(Figure):
    def __init__(self, radius):
        self.radius = radius

    def area(self):
        return math.pi * self.radius**2

class Triangle(Figure):
    def __init__(self, base, height):
        self.base = base
        self.height = height

    def area(self):
        return 0.5 * self.base * self.height

class Trapezoid(Figure):
    def __init__(self, base1, base2, height):
        self.base1 = base1
        self.base2 = base2
        self.height = height

    def area(self):
        return 0.5 * (self.base1 + self.base2) * self.height

rectangle = Rectangle(5, 8)
circle = Circle(4)
triangle = Triangle(6, 10)
trapezoid = Trapezoid(3, 7, 4)

figures = [rectangle, circle, triangle, trapezoid]

for figure in figures:
    print(f"{str(figure)} - Area: {figure.area()}, Int: {int(figure)}")