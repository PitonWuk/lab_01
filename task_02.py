"""
Завдання 2
Використовуючи механізм множинного успадкування, створіть клас «Автомобіль». Також мають бути класи:
«Колеса», «Двигун», «Двері» та ін.
"""
class Wheels:
    def __init__(self, count):
        self.count = count

class B(A):
    def go(self):
        super(B, self).stop()
        print("go B go!")
class Engine:
    def __init__(self, power):
        self.power = power

class Doors:
    def __init__(self, open = False):
        self.open = open

class C(A):
    def go(self):
        super(C, self).go()
        print("go C go!")
    def stop(self):
        super(C, self).stop()
        print("stop C stop!")
class Car(Wheels, Engine, Doors):
    def __init__(self, count, power, open):
        Wheels.__init__(self, count)
        Engine.__init__(self, power)
        Doors.__init__(self, open)


class E(B,C):
    pass

e=E()
e.go()
car = Car(4, 150, True)
print(car.__dict__)