"""
Завдання 2
 Створіть клас Circle з атрибутом radius та методом
area, який поверне площу кола з вказаним радіусом.

"""
class Circle:
    def __init__(self, radius):
        self.radius = radius

    def area(self):
        circle_area = 3.14 * (self.radius ** 2)
        print(f"Area = {circle_area}")

area1 = Circle(5)
area1.area()
