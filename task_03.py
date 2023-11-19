"""
Завдання 3
Запрограмуйте клас Money (об’єкт класу оперує однією
валютою) для роботи з грошима.
У класі мають бути передбачені: поле для зберігання цілої
частини грошей (долари, євро, гривні тощо) і поле для зберігання копійок (центи, євроценти, копійки тощо).
Реалізуйте методи виведення суми на екран, задання
значень частин.
Створіть клас Product для роботи з продуктом або товаром беручи за основу клас Money. Реалізуйте метод для
зменшення ціни на задане число.
Для кожного з класів реалізуйте необхідні методи та поля
"""
class Money:
    def __init__(self, currency, whole_part=0, fractional_part=0):
        self.currency = currency
        self.whole_part = whole_part
        self.fractional_part = fractional_part

    def display_amount(self):
        print(f"Total amount: {self.whole_part}.{self.fractional_part:02d} {self.currency}")

    def set_amount(self, whole_part, fractional_part):
        self.whole_part = whole_part
        self.fractional_part = fractional_part

class Product:
    def __init__(self, name, price):
        self.name = name
        self.price = price

    def decrease_price(self, amount):
        current_whole_part = self.price.whole_part
        current_fractional_part = self.price.fractional_part


        total_fractional_amount = current_whole_part * 100 + current_fractional_part
        total_fractional_amount -= amount

        if total_fractional_amount < 0:
            print("Price cannot be negative. Keeping the original price.")
        else:
            new_whole_part = total_fractional_amount // 100
            new_fractional_part = total_fractional_amount % 100

            self.price.set_amount(new_whole_part, new_fractional_part)

    def display_price(self):
        print(f"The price for {self.name} is: {self.price.whole_part}.{self.price.fractional_part:02d} {self.price.currency}")

money = Money(currency="USD", whole_part=20, fractional_part=50)
money.display_amount()

product = Product(name="Laptop", price=Money(currency="USD", whole_part=1500, fractional_part=75))
product.display_price()

product.decrease_price(1000)
product.display_price()
