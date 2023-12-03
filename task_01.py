"""
Завдання 1
 Метаклас, який вносить додаткові перевірки/логіку
до певних методів у всіх класах.
"""


class MyMetaClass(type):
    def __new__(cls, name, bases, dct):

        original_method = dct.get('my_method', None)

        if original_method:
            def new_method(self, *args, **kwargs):
                print(f"The method is called {name}.my_method with additional logic.")


                return original_method(self, *args, **kwargs)

            dct['my_method'] = new_method

        return super().__new__(cls, name, bases, dct)

class MyClass(metaclass=MyMetaClass):
    def my_method(self):
        print("The original method is called my_method.")


obj = MyClass()
obj.my_method()