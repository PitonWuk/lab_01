"""
Завдання 1
Створіть клас Device, який містить інформацію про пристрій.
За допомогою механізму успадкування реалізуйте клас
Coffee Machine (містить інформацію про кавомашину), клас
Blender (містить інформацію про блендер), клас MeatGrinder
(містить інформацію про м’ясорубку).
Кожен із класів має містити необхідні для роботи методи.
"""
class Device:
    def __init__(self, brand, model):
        self.brand = brand
        self.model = model

class CoffeeMachine(Device):
    def make_coffee(self):
        print(f"{self.brand} {self.model} is making coffee")

class Blender(Device):
    def blend(self):
        print(f"{self.brand} {self.model} is blending")

class MeatGrinder(Device):
    def grind_meat(self):
        print(f"{self.brand} {self.model} is grinding meat")

coffee_machine = CoffeeMachine(brand="CoffeeMaster", model="CM100")
blender = Blender(brand="BlendX", model="BX200")
meat_grinder = MeatGrinder(brand="GrindPro", model="GP300")

coffee_machine.make_coffee()
blender.blend()
meat_grinder.grind_meat()
