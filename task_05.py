"""
Завдання 5
Для класів із попереднього завдання реалізуйте магічний метод str, а також метод int (який повертає вік
службовця).
"""
from datetime import datetime
class Employer:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def Print(self):
        print("This is Employer class")

    def __str__(self):
        return f"{self.name} is from {self.age} year"

    def get_age(self):
        current_year = datetime.now().year
        return current_year - self.age

class President(Employer):
    def Print(self):
        print("This is President class")


class Manager(Employer):
    def Print(self):
        print("This is Manager class")

class Worker(Employer):
    def Print(self):
        print("This is Worker class")

employer = Employer("Tareck", 1988)
president = President("Clinton", 1935)
manager = Manager("Tomas", 1992)
worker = Worker("Anna", 1989)


employers = [employer, president, manager, worker]
for employer in employers:
    print(employer)
    print(f"Age: {employer.get_age()} years")
    employer.Print()
    print()
