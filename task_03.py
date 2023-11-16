"""
Завдання 3
Створіть базовий клас «Тварина» та похідні класи:
«Тигр», «Крокодил», «Кенгуру». Встановіть за допомогою
конструктора ім’я кожної тварини та її характеристики.
Створіть для кожного класу необхідні методи та поля.
"""
class Animal:
    def __init__(self, name, species):
        self.name = name
        self.species = species

    def display_info(self):
        print(f"Name: {self.name}\nSpecies: {self.species}")

class Tiger(Animal):
    def __init__(self, name, color):
        super().__init__(name, species="Tiger")
        self.color = color

    def make_sound(self):
        print("Roar!")

    def display_info(self):
        super().display_info()
        print(f"Color: {self.color}")

class Crocodile(Animal):
    def __init__(self, name, size):
        super().__init__(name, species="Crocodile")
        self.size = size

    def make_sound(self):
        print("Grunt!")

    def display_info(self):
        super().display_info()
        print(f"Size: {self.size}")

class Kangaroo(Animal):
    def __init__(self, name, jump_height):
        super().__init__(name, species="Kangaroo")
        self.jump_height = jump_height

    def make_sound(self):
        print("Boing!")

    def display_info(self):
        super().display_info()
        print(f"Jump Height: {self.jump_height}")


tiger = Tiger(name="Tiger", color="Orange")
crocodile = Crocodile(name="Crocodile", size="Large")
kangaroo = Kangaroo(name="Kangaroo", jump_height="High")

animals = [tiger, crocodile, kangaroo]

for animal in animals:
    animal.display_info()
    animal.make_sound()
    print("\n")