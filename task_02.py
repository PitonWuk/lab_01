"""
Завдання 2
При старті програми з’являється меню з наступними
пунктами:
1. Завантаження даних;
2. Збереження даних;
3. Додавання даних;
4. Видалення даних.
Використайте список цілих як сховища даних. Також
застосуйте стиснення/розпакування даних.
"""
import gzip
import pickle
def load_data(filename):
    try:
        with gzip.open(filename, 'rb') as file:
            data = pickle.load(file)
            return data
    except FileNotFoundError:
        return []

def save_data(data, filename):
    with gzip.open(filename, 'wb') as file:
        pickle.dump(data, file)

def add_data(data, item):
    data.append(item)

def remove_data(data, item):
    if item in data:
        data.remove(item)
        print(f"Eelement {item} deleted.")
    else:
        print(f"Element {item} was not found.")

def menu():
    data_filename = "data.gz"
    data = load_data(data_filename)

    while True:
        print("\nMenu:")
        print("1. Load data")
        print("2. Save data")
        print("3. Add data")
        print("4. Delete data")
        print("0. Exit")

        choice = input("Make your choice: ")
        if choice == '1':
            data = load_data(data_filename)
            print("Data loaded.")

        elif choice == '2':
            save_data(data, data_filename)
            print("Data saved.")

        elif choice == '3':
            item = int(input('Enter integer number for adding: '))
            add_data(data, item)
            print("Data added.")

        elif choice == '4':
            item = int(input('Enter integer number for delete: '))
            remove_data(data, item)
            print("Data deleted.")

        elif choice == '0':
            save_data(data, data_filename)
            print("Thank you! \nData saved.")
            break

        else:
            print("Try again!")

menu()


