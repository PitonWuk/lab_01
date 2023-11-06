"""
Завдання 2
Створіть клас «Місто». Збережіть у класі: назву міста,
назву регіону, назву країни, кількість жителів у місті,
поштовий індекс міста, телефонний код міста. Реалізуйте
методи класу для введення-виведення даних та інших
операцій.
"""

class City:
    def __init__(self, name, region, country, citizens, index, phone_code):
        self.name = name
        self.region = region
        self.country = country
        self.citizens = citizens
        self.index = index
        self.phone_code = phone_code

    def display_info(self):
        print(f"Name: {self.name}")
        print(f"Region: {self.region}")
        print(f"Country: {self.country}")
        print(f"Citizens: {self.citizens}")
        print(f"Index: {self.index}")
        print(f"Phone_code: {self.phone_code}")

    def change_phone_code(self, new_code):
        self.phone_code = new_code
        print(f"Phone code number was changed to: {new_code}")

city = City("Kyiv", "Kyiv region", "Ukraine", "200000 citizens", "35800", "044")
city.display_info()
city.change_phone_code("055")

city.display_info()
