"""
Завдання 2
Створіть клас для підрахунку площі геометричних
фігур. Клас має надавати функціональність підрахунку
площі трикутника за різними формулами, площі прямокутника, площі квадрата, площі ромба. Методи класу для
підрахунку площі реалізуйте за допомогою статичних
методів. Також клас має розрахувати кількість підрахунків площі та повернути це значення статичним методом.
"""
class AreaCalculator:
    count_of_calculation = 0

    @staticmethod
    def triangle_area(a, h):
        AreaCalculator.count_of_calculation += 1
        return 0.5 * h * a

    @staticmethod
    def rectangle_area(a, b):
        AreaCalculator.count_of_calculation += 1
        return a * b

    @staticmethod
    def square_area(a):
        AreaCalculator.count_of_calculation += 1
        return a ** 2

    @staticmethod
    def rhombus_area(diagonal1, diagonal2):
        AreaCalculator.count_of_calculation += 1
        return 0.5 * diagonal1 * diagonal2


triangle = AreaCalculator.triangle_area(2, 5)
rectangle = AreaCalculator.rectangle_area(3, 8)
square = AreaCalculator.square_area(3)
rhombus = AreaCalculator.rhombus_area(10, 13)
print(triangle)
print(rectangle)
print(square)
print(rhombus)
print("Quantity", AreaCalculator.count_of_calculation)




