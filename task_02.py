"""
Завдання 2
Використовуючи механізм множинного успадкування, створіть клас «Автомобіль». Також мають бути класи:
«Колеса», «Двигун», «Двері» та ін.
"""
class Wheels:
    def __init__(self, brand, size):
        self.brand = brand
        self.size = size

    def display_info(self):
        print(f"Wheels: Brand - {self.brand}, Size - {self.size}")


class Engine:
    def __init__(self, fuel_type, horsepower):
        self.fuel_type = fuel_type
        self.horsepower = horsepower

    def display_info(self):
        print(f"Engine: Fuel Type - {self.fuel_type}, Horsepower - {self.horsepower}")


class Doors:
    def __init__(self, number, style):
        self.number = number
        self.style = style

    def display_info(self):
        print(f"Doors: Number - {self.number}, Style - {self.style}")


class Car(Wheels, Engine, Doors):
    def __init__(self, brand, size, fuel_type, horsepower, number_of_doors, door_style):
        Wheels.__init__(self, brand, size)
        Engine.__init__(self, fuel_type, horsepower)
        Doors.__init__(self, number_of_doors, door_style)

    def display_car_info(self):
        print("Car Information:")
        self.display_info()

my_car = Car(brand="Michelin", size=18, fuel_type="Gasoline", horsepower=200, number_of_doors=4, door_style="Sedan")
my_car.display_car_info()