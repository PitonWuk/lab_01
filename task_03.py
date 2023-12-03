"""
Завдання 3
 Створіть метаклас, який автоматично додає певні
атрибути до всіх класів, що використовують його.
"""
class AutoAttributesMeta(type):
    def __new__(cls, name, bases, dct):
        dct['added_attribute'] = 'value'

        new_class = super().__new__(cls, name, bases, dct)
        return new_class

class MyClass(metaclass=AutoAttributesMeta):
    pass

print(MyClass.added_attribute)

