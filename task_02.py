"""
Завдання 2
До вже реалізованого класу «Місто» додайте конструктор та необхідні перевантажені методи.
"""
class City:
    def __init__(self, name, population, country):
        self.name = name
        self.population = population
        self.country = country

    def __str__(self):
        return f'Name: {self.name}, Population: {self.population}, Country: {self.country}'

    def __eq__(self, other):
        return (self.name == other.name and self.population == other.population and self.country)

    def __ne__(self, other):
        return not self.__eq__(other)

city1 = City('Kyiv', 300000, "Ukraine")
city2 = City('Lviv', 750000, 'Ukraine')

print(city1)
print(city1 == city2)
print(city1 != city2)
