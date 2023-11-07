"""
Завдання 3
До вже реалізованого класу «Країна» додайте конструктор та необхідні перевантажені методи.

"""
class Country:
    def __init__(self, name, continent, population, phone_code, capital, cities):
        self.name = name
        self.continent = continent
        self.population = population
        self.phone_code = phone_code
        self.capital = capital
        self.cities = cities

    def __str__(self):
        return f"Country: {self.name}, Continent: {self.continent}, Population: {self.population}, " \
               f"Phone_cod: {self.phone_code}, Capital: {self.capital}, Cities: {', '.join(self.cities)}"

    def __eq__(self, other):
        return (self.name == other.name
                and self.continent == other.continent
                and self.population == other.population
                and self.phone_code == other.phone_code
                and self.capital == other.capital
                and self.cities == other.cities)

    def __ne__(self, other):
        return not self.__eq__(other)

    def __len__(self):
        return len(self.cities)

country1 = Country("Ukraine", "Europa", 44000000, "+380", "Kyiv", ["Kyiv", "Lviv", "Odessa"])
country2 = Country("Polish", "Europa", 38000000, "+48", "Warsaw", ["Warsaw", "Krakow", "Lodz"])

print(country1)
print(len(country1))
print(country1 == country2)
print(country1 != country2)

