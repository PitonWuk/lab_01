"""
Завдання 1
Створіть клас Human, який міститиме інформацію
про людину.
За допомогою механізму успадкування реалізуйте
клас Builder (містить інформацію про будівельника),
клас Sailor (містить інформацію про моряка), клас Pilot
(містить інформацію про льотчика).
Кожен із класів має містити необхідні для роботи
методи.

"""
class Human:
    def __init__(self, name, age):
        self.name = name
        self.age = age

class Builder(Human):
    def __init__(self, name, age, skill):
        super().__init__(name, age)
        self.skill = skill

    def build(self):
        print(f"{self.name} is building something with skill {self.skill}")

class Sailor(Human):
    def __init__(self, name, age, sailing_experience):
        super().__init__(name, age)
        self.sailing_experience = sailing_experience

    def sailor(self):
        print(f"{self.name} is sailing with {self.sailing_experience} years of experience")

class Pilot(Human):
    def __init__(self, name, age, flying_experience):
        super().__init__(name, age)
        self.flying_experience = flying_experience

    def fly(self):
        print(f"{self.name} is flying with {self.flying_experience} years of experience.")

builder = Builder("Jon", 33, "Expert")
sailor = Sailor('Tom', 38, 20)
pilot = Pilot("Nina", 39, 10)

builder.build()
sailor.sailor()
pilot.fly()
