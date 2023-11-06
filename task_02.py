"""
Завдання 2
 Реалізуйте клас «Стадіон». Збережіть у класі: назву
стадіону, дату відкриття, країну, місто, місткість. Реалізуйте
методи класу для введення-виведення даних та інших
операцій. До вже реалізованого класу «Стадіон» додайте
необхідні перевантажені методи та оператори.
"""
class Stadium:
    def __init__(self, name, opening_date, country, city, capacity):
        self.name = name
        self.opening_date = opening_date
        self.country = country
        self.city = city
        self.capacity = capacity


    def display_info(self):
        print(f"Stadium: {self.name}")
        print(f"Opening date: {self.opening_date}")
        print(f"Country: {self.country}")
        print(f"City: {self.city}")
        print(f"Capacity: {self.capacity}")

    def __str__(self):
        return f"{self.name} ({self.city}, {self.country}) - Capacity: {self.capacity}"


stadium1 = Stadium("Olimpijski", "1923", "Ukraine", "Kyiv", 70050)
stadium1.display_info()

print(str(stadium1))
