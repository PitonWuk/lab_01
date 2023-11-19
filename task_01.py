"""
Завдання 1
Використовуючи поняття множинного успадкування,
створіть клас «Коло, поміщене в квадрат».
"""
import math

class Square:
    def __init__(self, side_length):
        self.side_length = side_length

    def area(self):
        return self.side_length ** 2

    def display_info(self):
        print(f"Square: Side Length - {self.side_length}, Area - {self.area()}")


class CircleInSquare(Square):
    def __init__(self, side_length, radius):
        super().__init__(side_length)
        self.radius = radius

    def area(self):
        return math.pi * self.radius ** 2

    def display_info(self):
        print(f"Circle in Square:")
        super().display_info()
        print(f"Circle: Radius - {self.radius}, Area - {self.area()}")


circle_in_square = CircleInSquare(side_length=4, radius=2)
circle_in_square.display_info()