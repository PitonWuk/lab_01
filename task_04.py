"""
Завдання 4
Створіть базовий клас Employer (службовець) з функцією Print(). Функція має виводити інформацію про службовця.
Для базового класу це може бути рядок із написом «This is Employer class».
Створіть від нього три похідні класи: President, Manager, Worker. Перевизначте функцію Print() для виведення
інформації, що відповідає кожному типу службовця.
"""
class Employer:
    def __init__(self, name, sex, age):
        self.name = name
        self.sex = sex
        self.age = age

    def display_info(self):
        print(f"{self.name} is a {self.sex} and has {self.age} years old")

class President(Employer):
    def __init__(self, name, sex, age, president):
        super().__init__(name, sex, age)
        self.president = president

    def display_info(self):
        print(f"{self.name} is a {self.sex} and has {self.age} years old. He/She is a {self.president}")

class Manager(Employer):
    def __init__(self, name, sex, age, manager):
        super().__init__(name, sex, age)
        self.manager = manager

    def display_info(self):
        print(f"{self.name} is a {self.sex} and has {self.age} years old. He/She is a {self.manager}")

class Worker(Employer):
    def __init__(self, name, sex, age, worker):
        super().__init__(name, sex, age)
        self.worker = worker

    def display_info(self):
        print(f"{self.name} is a {self.sex} and has {self.age} years old. He/She is a {self.worker}")

president = President("Clinton", "male", 65, "president")
manager = Manager("Tomas", "male", 33, "manager")
worker = Worker("Anna", "female", 25, "worker")

president.display_info()
manager.display_info()
worker.display_info()





