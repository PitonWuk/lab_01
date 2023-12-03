"""
Завдання 4
Метаклас, що додає перевірку та обробку аргументів
__init__ у всіх класах.
"""

class InitArgsMeta(type):
    def __new__(cls, name, bases, dct):
        init_args = dct.get('init_args', None)

        if init_args:
            original_init = dct.get('__init__', None)

            def new_init(self, *args, **kwargs):
                for arg_name in init_args:
                    if arg_name in kwargs:
                        value = kwargs[arg_name]
                        if not isinstance(value, int):
                            raise TypeError(f"{arg_name} must be an integer.")

                if original_init:
                    original_init(self, *args, **kwargs)

            dct['__init__'] = new_init

        return super().__new__(cls, name, bases, dct)

class MyClass(metaclass=InitArgsMeta):
    init_args = ['value']

    def __init__(self, value):
        self.value = value

obj = MyClass(value=42)
print(obj.value)

try:
    invalid_obj = MyClass(value="invalid")
except TypeError as e:
    print(f"TypeError: {e}")
