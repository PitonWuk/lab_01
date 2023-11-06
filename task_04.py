"""
Завдання 4
До вже реалізованого класу «Книга» додайте
необхідні перевантажені методи та оператори.
"""
class Book:
    def __init__(self, title, author, pages):
        self.title = title
        self.author = author
        self.pages = pages

    def __str__(self):
        return f"{self.title} by {self.author}"

    def __eq__(self, other):
        return self.title == other.title and self.author == other.author

    def __lt__(self, other):
        return self.title < other.title

    def __len__(self):
        return self.pages

    def __add__(self, other):
        if isinstance(other, int):
            return Book(self.title, self.author, self.pages + other)
        else:
            return Book(f"{self.title} and {other.title}", self.author, self.pages + other.pages)


book1 = Book("Book 1", "Author 1", 100)
book2 = Book("Book 2", "Author 2", 150)

print(book1)

print(book1 == book2)
print(book1 < book2)

print(len(book1))

combined_book = book1 + book2
print(combined_book.pages)

extended_book = book1 + 50
print(extended_book.pages)