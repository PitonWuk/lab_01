"""
Завдання 1
Створіть клас Student з атрибутами name та age.
Додайте метод print_info, який виведе інформацію про
студента у на вигляді "Ім'я: {name}, Вік: {age}".
"""

class Student:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def print_info(self):
        print(f"Name: {self.name}, Age: {self.age}")

student = Student("Mark", 23)
student.print_info()



