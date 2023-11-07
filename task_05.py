"""
Завдання 5
Реалізуйте клас «Вебсайт». Збережіть у класі: назву
вебсайту, адресу та опис вебсайту. Реалізуйте конструктор
та методи класу для введення-виведення даних, а також
для інших операцій. Використовуйте механізм перевантаження методів.
"""
class Website:
    def __init__(self, name, url, description):
        self.name = name
        self.url = url
        self.description = description

    def __str__(self):
        return f"Name: {self.name}\nURL: {self.url}\nDescription: {self.description}"

    def __eq__(self, other):
        return (
            self.name == other.name
            and self.url == other.url
            and self.description == other.description
        )

    def set_attributes(self, name, url, description):
        self.name = name
        self.url = url
        self.description = description

website1 = Website("Google", "https://www.google.com", "Search system")

website1.set_attributes("YouTube", "https://www.youtube.com", "Video")

print(website1)