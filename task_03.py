"""
Завдання 3
Створіть клас для підрахунку максимуму з чотирьох
аргументів, мінімуму з чотирьох аргументів, середнє
арифметичне із чотирьох аргументів, факторіалу аргументу. Реалізуйте функціональність у вигляді статичних
методів.
"""

class Maximum:
    count_of_calculation = 0

    @staticmethod
    def max_elements(a, b, c, d):
        Maximum.count_of_calculation += 1
        return max(a, b, c, d)

    @staticmethod
    def min_elements(a, b, c, d):
        Maximum.count_of_calculation += 1
        return min(a, b, c, d)

    @staticmethod
    def mid_elements(a, b, c, d,):
        Maximum.count_of_calculation += 1
        return (a + b + c + d) / 4

    @staticmethod
    def fact_elements(n):
        Maximum.count_of_calculation += 1
        if n == 0 or n == 1:
            return 1
        else:
            return n * Maximum.fact_elements(n - 1)

numbers = (6, 14, 8, 4)

max_elements = Maximum.max_elements(*numbers)
min_elements = Maximum.min_elements(*numbers)
mid_elements = Maximum.mid_elements(*numbers)
fact_elements = Maximum.fact_elements(6)

print("Maximum: ", max_elements)
print("Minimum: ", min_elements)
print("Middle: ", mid_elements)
print("Factorial: ", fact_elements)

print("Quantity: ", Maximum.count_of_calculation)
