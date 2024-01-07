"""
Завдання 2
Змініть стек із першого завдання таким чином, щоб його
розмір був нефіксованим.

"""
class DynamicStringStack:
    def __init__(self):
        self.stack = []

    def push(self, value):
        self.stack.append(value)
        print("Рядок додано до стеку.")

    def pop(self):
        if not self.is_empty():
            popped_value = self.stack.pop()
            print(f"Рядок '{popped_value}' виштовхнуто зі стеку.")
        else:
            print("Стек порожній. Немає рядків для виштовхування.")

    def count(self):
        return len(self.stack)

    def is_empty(self):
        return len(self.stack) == 0

    def clear(self):
        self.stack.clear()
        print("Стек очищено.")

    def peek(self):
        if not self.is_empty():
            return self.stack[-1]
        else:
            print("Стек порожній. Немає рядків для перегляду.")

# Функція для відображення меню
def display_menu():
    print("Меню:")
    print("1. Додати рядок у стек")
    print("2. Виштовхнути рядок зі стеку")
    print("3. Кількість рядків у стеку")
    print("4. Очистити стек")
    print("0. Вийти")

# Основна програма
def main_dynamic_stack():
    stack = DynamicStringStack()

    while True:
        display_menu()
        choice = input("Виберіть операцію (0-4): ")

        if choice == "0":
            print("Дякую за використання програми. До побачення!")
            break
        elif choice == "1":
            value = input("Введіть рядок для додавання до стеку: ")
            stack.push(value)
        elif choice == "2":
            stack.pop()
        elif choice == "3":
            print("Кількість рядків у стеку:", stack.count())
        elif choice == "4":
            stack.clear()
        else:
            print("Невірний вибір. Спробуйте ще раз.")

main_dynamic_stack()
