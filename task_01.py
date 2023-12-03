"""
Завдання 1
Задайте метаклас, що автоматично додає
додатковий функціонал до всіх класів, що його
використовують.
"""
class AdditionalFunctionalityMeta(type):
    def __new__(cls, name, bases, dct):

        dct['additional_functionality'] = lambda obj: print("Additional functionality for the object", obj)

        new_class = super().__new__(cls, name, bases, dct)
        return new_class

class MyClass(metaclass=AdditionalFunctionalityMeta):
    pass

obj = MyClass()
obj.additional_functionality()


