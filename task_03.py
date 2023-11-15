"""
Завдання 3
Створіть базовий клас «Домашня тварина» та похідні
класи «Пес», «Кіт», «Папуга», «Хом’як». За допомогою
конструктора встановіть ім’я кожної тварини та її характеристики. Реалізуйте для кожного із класів наступні
методи:
■ Sound — видає звук тварини (пишемо текстом в консоль);
■ Show — відображає ім’я тварини;
■ Type — відображає підвид тварини.
"""
class DomesticAnimal:
    def __init__(self, name):
        self.name = name

    def sound(self):
        pass

    def show(self):
        print(f"Name {self.name}")

class Dog(DomesticAnimal):
    pass

class Cat(DomesticAnimal):
    pass

class Parrot(DomesticAnimal):
    pass

class Hamster(DomesticAnimal):
    pass

|||||||||||||||||||||||||||||||||||||||||||||||||

from dataclasses import dataclass


@dataclass
class DomesticAnimal:
    _name: str
    _type_of_animal: str

    def sound(self):
        pass

    def show(self):
        print(f'{self._name}')

    def type_of_animal(self):
        print(self._type_of_animal)


@dataclass
class Dog(DomesticAnimal):
    def sound(self):
        print('Gav-Gav-Gav')


@dataclass
class Cat(DomesticAnimal):
    def sound(self):
        print('Miau-Miau')


@dataclass
class Perrot(DomesticAnimal):
    def sound(self):
        print('Kria-Kria')


@dataclass
class Hamster(DomesticAnimal):
    def sound(self):
        print('Nyam-Nyam')


dog = Dog('Hatiko', 'Dog')
cat = Cat('Matroskin', 'Cat')
parrot = Cat('Kesha', 'Parrot')
hamster = Hamster('Homyak', 'Hamster')

dog.sound()
dog.show()
dog.type_of_animal()
