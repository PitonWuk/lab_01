"""
Завдання 1
Створіть клас "Користувач" з атрибутами "ім'я", "вік" та
"email". Застосуйте інкапсуляцію, щоб забезпечити, що ці
дані можна отримати лише через методи класу.
"""

class User:
    def __init__(self, name, age, email):
        self.__name = name
        self.__age = age
        self.__email = email

    def get_name(self):
        return self.__name

    def get_age(self):
        return self.__age

    def get_email(self):
        return self.__email

user1 = User("John Doe", 25, "john.doe@example.com")

print("Name:", user1.get_name())
print("Age:", user1.get_age())
print("Email:", user1.get_email())
