"""
Завдання 1
До вже реалізованого класу «Людина» додайте статичний метод, який під час виклику повертає кількість
створених об’єктів класу «Людина».
"""
class Person:
    num_of_instances = 0
    def __init__(self, name, date, phone, city, country, address):
        self.name = name
        self.date = date
        self.phone = phone
        self.city = city
        self.country = country
        self.address = address
        Person.num_of_instances += 1

    @staticmethod
    def get_num_of_instances():
        return Person.num_of_instances

    def display_info(self):
        print(f"Name: {self.name}")
        print(f"Date: {self.date}")
        print(f"Phone: {self.phone}")
        print(f"City: {self.city}")
        print(f"Country: {self.country}")
        print(f"Address: {self.address}")

    def change_number(self, new_number):
        self.phone = new_number
        print(f"The number was updated to: {new_number}")

person = Person("Makr Seli", "02.03.1999", "+385232125236", "Kyiv", "Ukraine", "Sobornosty, 22")
person.display_info()

person.change_number("+36251244852")
person.display_info()

print(Person.num_of_instances)
