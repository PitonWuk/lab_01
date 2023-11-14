"""
Завдання 3
Створіть базовий клас «Тварина» та похідні класи:
«Тигр», «Крокодил», «Кенгуру». Встановіть за допомогою
конструктора ім’я кожної тварини та її характеристики.
Створіть для кожного класу необхідні методи та поля.
"""
class Animal:
    def __init__(self, name, species, sound):
        self.name = name
        self.species = species
        self.sound = sound

    def make_sound(self):
        print(f"{self.species} {self.name} make sound {self.sound}")

    def move(self):
        print(f"{self.species} {self.name} move")

class Tiger(Animal):
    def __init__(self, name):
        super().__init__(name, "Tiger", "Roar")

    def swim(self):
        super().swim()

tiged = Tiger("Sherhan")
tiged.swim()
