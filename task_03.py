"""
Завдання 3
Створіть базовий клас Shape для рисування плоских фігур.
Визначте методи:
■ Show() — виведення на екран інформації про фігуру;
■ Save() — збереження фігури у файл;
■ Load() — зчитування фігури з файлу.
Визначте похідні класи:
■ Square — квадрат із заданими з координатами лівого
верхнього кута та довжиною сторони.
■ Rectangle — прямокутник із заданими координатами
верхнього лівого кута та розмірами.
Circle — коло із заданими координатами центру та радіусом.
■ Ellipse — еліпс із заданими координатами верхнього кута
описаного навколо нього прямокутника зі сторонами,
паралельними осям координат, та розмірами цього прямокутника.
Створіть список фігур, збережіть фігури у файл, завантажте в інший список та відобразіть інформацію про кожну
фігуру
"""
import pickle

class Shape:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def show(self):
        print(f"Position: ({self.x}, {self.y})")

    def save(self, new_file):
        with open(new_file, 'wb') as file:
            pickle.dump(self, file)

    @classmethod
    def load(cls, new_file):
        with open(new_file, 'rb') as file:
            return pickle.load(file)

class Square(Shape):
    def __init__(self, x, y, side_length):
        super().__init__(x, y)
        self.side_length = side_length

    def show(self):
        super().show()
        print(f"Square with side length: {self.side_length}")

class Rectangle(Shape):
    def __init__(self, x, y, width, height):
        super().__init__(x, y)
        self.width = width
        self.height = height

    def show(self):
        super().show()
        print(f"Rectangle with width: {self.width} and height: {self.height}")

class Circle(Shape):
    def __init__(self, x, y, radius):
        super().__init__(x, y)
        self.radius = radius

    def show(self):
        super().show()
        print(f"Circle with radius: {self.radius}")

class Ellipse(Shape):
    def __init__(self, x, y, width, height):
        super().__init__(x, y)
        self.width = width
        self.height = height

    def show(self):
        super().show()
        print(f"Ellipse with width: {self.width} and height: {self.height}")

square = Square(0, 0, 5)
rectangle = Rectangle(0, 0, 8, 4)
circle = Circle(0, 0, 3)
ellipse = Ellipse(0, 0, 6, 4)

shapes = [square, rectangle, circle, ellipse]
for i, shape in enumerate(shapes):
    shape.save(f'shape_{i}.pickle')

loaded_shapes = [Shape.load(f'shape_{i}.pickle') for i in range(len(shapes))]

for loaded_shape in loaded_shapes:
    loaded_shape.show()
    print("--------")
