"""
Завдання 3
Створіть клас «Країна». Збережіть у класі: назву країни,
назву континенту, кількість жителів країни, телефонний
код країни, назву столиці, назву міст країни. Реалізуйте
методи класу для введення-виведення даних та інших
операцій.
"""
class Country:
    def __init__(self, name, continent, population, dialing_code, capital, cities):
        self.name = name
        self.continent = continent
        self.population = population
        self.dialing_code = dialing_code
        self.capital = capital
        self.cities = cities

    def display_info(self):
        print(f"Name of country: {self.name}")
        print(f"Name of continent: {self.continent}")
        print(f"Population: {self.population}")
        print(f"Code: +{self.dialing_code}")
        print(f"Capital: {self.capital}")
        print("Cities:")
        for city in self.cities:
            print(city)

    def add_city(self, city_name):
        self.cities.append(city_name)
        print(f"City {city_name} added to list.")

ukraine = Country("Ukraine", "Europe", 44000000, 380, "Kyiv", ["Kyiv", "Lviv", "Harkiv"])

ukraine.display_info()

ukraine.add_city("Odessa")

ukraine.display_info()