"""
Завдання 4
Реалізуйте клас «Годинник». Збережіть у класі:
назву моделі годинника, виробника годинника, рік
випуску, ціну годинника, тип годинника (наручний,
настінний і т. д.). Реалізуйте конструктор та методи
класу для введення-виведення даних, а також для
інших операцій. Використовуйте механізм
перевантаження методів.
"""

class Watch:
    def __init__(self, model, manufacturer, year, price, watch_type):
        self.model = model
        self.manufacturer = manufacturer
        self.year = year
        self.price = price
        self.watch_type = watch_type

    def __str__(self):
        return f"Model: {self.model}\nManufacturer: {self.manufacturer}\nYear: {self.year}" \
               f"\nPrice: {self.price}\nType: {self.watch_type}"

    def __eq__(self, other):
        return (
            self.model == other.model
            and self.manufacturer == other.manufacturer
            and self.year == other.year
            and self.price == other.price
            and self.watch_type == other.watch_type
        )

    def __lt__(self, other):
        return self.price < other.price

    def __gt__(self, other):
        return self.price > other.price

    def __add__(self, discount):
        return Watch(
            self.model,
            self.manufacturer,
            self.year,
            self.price - discount,
            self.watch_type,
        )

    def set_attributes(self, model, manufacturer, year, price, watch_type):
        self.model = model
        self.manufacturer = manufacturer
        self.year = year
        self.price = price
        self.watch_type = watch_type

watch1 = Watch("Omega Seamaster", "Omega", 2020, 2500, "hand")
watch2 = Watch("Rolex Submariner", "Rolex", 2019, 6000, "hand")

watch1.set_attributes("Rolex Submariner", "Rolex", 2019, 6000, "hand")

print(watch1)

if watch1 < watch2:
    print("Omega is cheaper than Rolex")
else:
    print("Rolex is expansive than Omega")

discounted_watch = watch1 + 200
print(f"Price after discount: {discounted_watch.price} USD")
