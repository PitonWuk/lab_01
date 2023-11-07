"""
Завдання 1
До вже реалізованого класу «Людина» додайте конструктор та необхідні перевантажені методи.
"""
class Person:
    def __init__(self, name, age, address):
        self.name = name
        self.age = age
        self.address = address

    def __str__(self):
        return f'Name: {self.name}, Age: {self.age}, Address: {self.address}'

    def __eq__(self, other):
        return (self.name == other.name and self.age == other.age and self.address == other.address)

    def __ne__(self, other):
        return not self.__eq__(other)

person1 = Person("Mark", 26, "Kyiv")
person2 = Person('Tom', 33, "Lviv")

print(person1)
print(person2)
print(person1 == person2)
print(person1 != person2)



