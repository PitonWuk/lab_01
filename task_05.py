"""
Завдання 5
Створіть клас Character, який має атрибути name, health
та damage. Реалізуйте метод класу attack, який виводить
повідомлення про атаку гравця.
"""

class Character:
    def __init__(self, name, health, damage):
        self.name = name
        self.health = health
        self.damage = damage

    @classmethod
    def attack(cls, value):
        print(f"The gamer {value.name} has {value.health} health points and attacked with power of {value.damage} points!")

value = Character ("Gamer1", 80, 110)
Character.attack(value)


