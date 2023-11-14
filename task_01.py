"""
Завдання 1
Завдання 1
До вже реалізованого класу «Дріб» додайте статичний метод, який при виклику повертає кількість створених об’єктів
класу «Дріб».
"""
class Fraction:
    number_of_objects = 0

    def __init__(self, numerator, denominator):
        self.numerator = numerator
        self.denominator = denominator
        Fraction.number_of_objects += 1

    @staticmethod
    def number_of_objects_created():
        return Fraction.number_of_objects

fraction1 = Fraction(5, 9)
fraction2 = Fraction(1, 4)

print(f"Number of created objects: {Fraction.number_of_objects_created()}")

