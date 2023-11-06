"""
Завдання 3
 До вже реалізованого класу «Автомобіль» додайте
необхідні перевантажені методи та оператори.
"""
class Car:
    def __init__(self, brand, model, year):
        self.brand = brand
        self.model = model
        self.year = year
        self.engine_started = False

    def start_engine(self):
        self.engine_started = True
        print(f"{self.year} {self.brand} {self.model}'s engine is started.")

    def __str__(self):
        return f"{self.year} {self.brand} {self.model}"

    def __eq__(self, other):
        return self.year == other.year and self.brand == other.brand and self.model == other.model

    def __ne__(self, other):
        return not self.__eq__(other)


car1 = Car("Toyota", "Camry", 2020)
car2 = Car("Honda", "Accord", 2020)

print(car1)
print(car2)

if car1 == car2:
    print("These cara are the same.")
else:
    print("These cars are different.")

car1.start_engine()
