"""
Завдання 2
Створіть клас Ship, який містить інформацію про кораблі.
За допомогою механізму успадкування реалізуйте клас
Frigate (містить інформацію про фрегат), клас Destroyer(містить
інформацію про есмінця), клас Cruiser (містить інформацію
про крейсер).
Кожен із класів має містити необхідні для роботи методи
"""
class Ship:
    def __init__(self, name, displacement):
        self.name = name
        self.displacement = displacement

    def sail(self):
        print(f"{self.name} is sailing.")

class Frigate(Ship):
    def __init__(self, name, displacement, missile_system):
        super().__init__(name, displacement)
        self.missile_system = missile_system

    def fire_missile(self):
        print(f"{self.name} is firing a missile from the {self.missile_system}.")

class Destroyer(Ship):
    def __init__(self, name, displacement, cannon_count):
        super().__init__(name, displacement)
        self.cannon_count = cannon_count

    def fire_cannons(self):
        print(f"{self.name} is firing {self.cannon_count} cannons.")

class Cruiser(Ship):
    def __init__(self, name, displacement, aircraft_count):
        super().__init__(name, displacement)
        self.aircraft_count = aircraft_count

    def launch_aircraft(self):
        print(f"{self.name} is launching {self.aircraft_count} aircraft.")


frigate = Frigate(name="Frigate1", displacement=1500, missile_system="Mars")
destroyer = Destroyer(name="Destroyer1", displacement=2000, cannon_count=50)
cruiser = Cruiser(name="Cruiser1", displacement=2200, aircraft_count=150)

frigate.fire_missile()
destroyer.fire_cannons()
cruiser.launch_aircraft()

