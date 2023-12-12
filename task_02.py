"""
Завдання 2
Створіть метаклас, що перевіряє наявність певних
атрибутів у всіх класах, які використовують цей
метаклас.

"""
class RequiredAttributesMeta(type):
    def __init__(cls, name, bases, dct):
        required_attributes = getattr(cls, 'required_attributes', [])

        for attribute in required_attributes:
            if attribute not in dct:
                raise AttributeError(f"Class {cls.__name__} should be attribute '{attribute}'.")

        super().__init__(name, bases, dct)

class MyClass1(metaclass=RequiredAttributesMeta):
    required_attributes = ['attr1', 'attr2']

    def __init__(self, attr1, attr2):
        self.attr1 = attr1
        self.attr2 = attr2

class MyClass2(metaclass=RequiredAttributesMeta):
    required_attributes = ['attr1', 'attr3']

    def __init__(self, attr1, attr3):
        self.attr1 = attr1
        self.attr3 = attr3

#obj1 = MyClass1(attr1='value1', attr2='value2')
obj2 = MyClass2(attr1='value1', attr3='value3')
