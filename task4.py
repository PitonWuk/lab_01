"""
Завдання 4
 Створіть клас Car з атрибутами brand (марка
автомобіля), model (модель) та year (рік випуску).
Додайте метод start_engine, який виведе повідомлення
про те, що двигун запущено.
"""
class Car:
    def __init__(self, brand, model, year):
        self.brand = brand
        self.model = model
        self.year = year

    def start_engine(self):
        print(f"Was started the engine for car: {self.brand} {self.model} with {self.year} year of production")

my_car = Car("Dodge", "Journey", 2023)
my_car.start_engine()
