"""
Завдання
Користувач вводить з клавіатури набір чисел. Отримані
числа необхідно зберегти до списку (тип списку оберіть в залежності від поставленого нижче завдання).
Після чого покажіть меню, в якому запропонуєте користувачеві набір пунктів:
1. Додати нове число до списку (якщо таке число існує у
списку, потрібно вивести повідомлення про це користувачеві без додавання числа).
2. Видалити усі входження числа зі списку (користувач вводить з клавіатури число для видалення)
3. Показати вміст списку (залежно від вибору користувача,
покажіть список з початку або з кінця)
4. Перевірити, чи є значення у списку
5. Замінити значення у списку (користувач визначає, чи
замінити тільки перше входження, чи всі)
Дія виконується залежно від вибору користувача, після
чого меню з’являється знову
"""
class NumberList:
    def __init__(self):
        self.numbers = []

    def add_number(self, number):
        if number not in self.numbers:
            self.numbers.append(number)
            print(f"Number {number} added to the list.")
        else:
            print(f"Number {number} already in the list.")

    def remove_number(self, number):
        if number in self.numbers:
            self.numbers.remove(number)
            print(f"Number {number} removed from the list.")
        else:
            print(f"Number {number} not in the list.")

    def show_list(self, reverse=False):
        if reverse:
            print("List contents (from the end):", self.numbers[::-1])
        else:
            print("List contents (from the beginning):", self.numbers)

    def check_number(self, number):
        if number in self.numbers:
            print(f"Number {number} is in the list.")
        else:
            print(f"Number {number} is not in the list.")

    def replace_number(self, old_number, new_number, replace_all=False):
        if old_number in self.numbers:
            if replace_all:
                self.numbers = [new_number if num == old_number else num for num in self.numbers]
            else:
                index = self.numbers.index(old_number)
                self.numbers[index] = new_number

            print(f"Number {old_number} replaced by {new_number}.")
        else:
            print(f"Number {old_number} is not in the list.")

number_list = NumberList()

while True:
    print("\nMenu:")
    print("1. Add a new number to the list")
    print("2. Remove all occurrences of a number from the list")
    print("3. Show list contents")
    print("4. Check if the value is in the list")
    print("5. Replace a value in a list")
    print("0. Exit the program")

    choice = input("Select the option: ")

    if choice == "1":
        number = int(input("Enter the number to add: "))
        number_list.add_number(number)
    elif choice == "2":
        number = int(input("Enter the number to delete: "))
        number_list.remove_number(number)
    elif choice == "3":
        reverse_order = input("Print the list in reverse order? (y/n): ").lower() == 'y'
        number_list.show_list(reverse=reverse_order)
    elif choice == "4":
        number = int(input("Enter the number to check: "))
        number_list.check_number(number)
    elif choice == "5":
        old_number = int(input("Enter the number to replace: "))
        new_number = int(input("Enter a new number: "))
        replace_all = input("Replace all occurrences? (y/n): ").lower() == 'y'
        number_list.replace_number(old_number, new_number, replace_all)
    elif choice == "0":
        print("The program is completed.")
        break
    else:
        print("Wrong choice. Please try again.")
