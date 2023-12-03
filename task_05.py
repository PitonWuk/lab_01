"""
Завдання 5
 Створіть клас Multiplier, який при ініціалізації
отримує множник. Забезпечте можливість викликати
цей об'єкт з аргументом та повертати множене
значення.
"""
class Multiplier:
    def __init__(self, factor):
        self.factor = factor

    def __call__(self, x):
        return x * self.factor

multiplier_by_2 = Multiplier(factor=3)
result = multiplier_by_2(8)

print(result)