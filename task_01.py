"""
Завдання 1
Створіть клас Calculator, який може виконувати
операції додавання, віднімання, множення та ділення.
Кожна операція буде реалізована як метод класу.
Об'єкт класу Calculator буде функтором, що може
викликатися для виконання обраної операції.
"""
class Calculator:
    def add(self, x, y):
        return x + y

    def subtract(self, x, y):
        return x - y

    def multiply(self, x, y):
        return x * y

    def divide(self, x, y):
        if y != 0:
            return x / y
        else:
            raise ValueError("Division by zero is not possible.")

    def __call__(self, operation, x, y):

        if operation == 'add':
            return self.add(x, y)
        elif operation == 'subtract':
            return self.subtract(x, y)
        elif operation == 'multiply':
            return self.multiply(x, y)
        elif operation == 'divide':
            return self.divide(x, y)
        else:
            raise ValueError("Incorrect operation.")

calculator = Calculator()

result = calculator('add', 15, 8)
print("Addition:", result)

result = calculator('subtract', 5, 3)
print("Subtraction:", result)

result = calculator('multiply', 5, 7)
print("Multiplication:", result)

result = calculator('divide', 5, 3)
print("Division:", result)
