"""
Завдання 1
Реалізуйте клас стеку для роботи з рядками (стек рядків).
Стек має бути фіксованого розміру. Реалізуйте набір операцій
для роботи зі стеком:
o розміщення рядка у стек;
o виштовхування рядка зі стеку;
o підрахунок кількості рядків у стеку;
o перевірку, чи порожній стек;
o перевірку, чи повний стек;
o очищення стеку;
o отримання значення без виштовхування
верхнього рядка зі стеку.
На старті додатка відобразіть меню, в якому користувач
може вибрати необхідну операцію.

"""
class StringStack:
    def __init__(self, max_size):
        self.max_size = max_size
        self.stack = []

    def push(self, value):
        if len(self.stack) < self.max_size:
            self.stack.append(value)
            print("Рядок додано до стеку.")
        else:
            print("Стек повний. Рядок не може бути доданий.")

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

    def is_full(self):
        return len(self.stack) == self.max_size

    def clear(self):
        self.stack.clear()
        print("Стек очищено.")

    def peek(self):
        if not self.is_empty():
            return self.stack[-1]
        else:
            print("Стек порожній. Немає рядків для перегляду.")


def display_menu():
    print("Меню:")
    print("1. Додати рядок у стек")
    print("2. Виштовхнути рядок зі стеку")
    print("3. Кількість рядків у стеку")
    print("4. Перевірити, чи порожній стек")
    print("5. Перевірити, чи повний стек")
    print("6. Очистити стек")
    print("7. Отримати значення верхнього рядка без виштовхування")
    print("0. Вийти")


def main():
    max_size = int(input("Введіть максимальний розмір стеку: "))
    stack = StringStack(max_size)

    while True:
        display_menu()
        choice = input("Виберіть операцію (0-7): ")

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
            print("Стек порожній:", stack.is_empty())
        elif choice == "5":
            print("Стек повний:", stack.is_full())
        elif choice == "6":
            stack.clear()
        elif choice == "7":
            top_value = stack.peek()
            if top_value is not None:
                print("Значення верхнього рядка без виштовхування:", top_value)
        else:
            print("Невірний вибір. Спробуйте ще раз.")

main()
