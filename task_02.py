"""
Завдання 2
 Метаклас, що може змінювати ім'я класу залежно
від певних умов або параметрів.

"""
class PrefixMetaClass(type):
    def __new__(cls, name, bases, dct):
        add_prefix = dct.get('add_prefix', False)

        if add_prefix:
            name = "Prefixed_" + name
        return super().__new__(cls, name, bases, dct)

class MyClass(metaclass=PrefixMetaClass):
    add_prefix = True

print(MyClass.__name__)
