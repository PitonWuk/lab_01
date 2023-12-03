"""
Завдання 4
Створіть клас для представлення користувача з
атрибутами: ім'я та вік. Додайте властивості для
валідації віку користувача. Наприклад, вік повинен
бути у межах від 0 до 120.
"""
class User:
    def __init__(self, name, age):
        self.name = name
        self._age = age

    @property
    def age(self):
        return self._age

    @age.setter
    def age(self, value):
        if 0 <= value <= 120:
            self._age = value
        else:
            raise ValueError("Invalid age. The age must be between 0 and 120.")

user = User(name="John", age=29)

print("Age:", user.age)

try:
    user.age = 30
    print("New age:", user.age)
except ValueError as e:
    print(f"Error: {e}")

try:
    user.age = 150
except ValueError as e:
    print(f"Error: {e}")
