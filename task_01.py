"""
Завдання 1
Маємо певний словник з назвами країн і столиць. Назва
країни використовується як ключ, назва столиці — як значення. Реалізуйте: додавання, видалення, пошук, редагування,
збереження та завантаження даних (використовуючи стиснення та розпакування).
"""
import gzip
import pickle

def load_data(filename):
    try:
        with gzip.open(filename, 'rb') as file:
            data = pickle.load(file)
            return data
    except FileNotFoundError:
        return {}

def save_data(data, filename):
    with gzip.open(filename, 'wb') as file:
        pickle.dump(data, file)

def add_country(data, country, capital):
    data[country] = capital
    print(f"Added: {country} — {capital}.")

def remove_country(data, country):
    if country in data:
        del data[country]
        print(f"Deleted: {country}.")
    else:
        print(f"Country {country} was not found.")

def search_country(data, country):
    if country in data:
        print(f"{country} — {data[country]}.")
    else:
        print(f"Country {country} was not found.")

def edit_country(data, country, new_capital):
    if country in data:
        data[country] = new_capital
        print(f"Edited: {country} — {new_capital}.")
    else:
        print(f"Country {country} was not found.")

def menu():
    data_filename = "countries_data.gz"
    countries_data = load_data(data_filename)

    while True:
        print("\nMenu:")
        print("1. Adding a country")
        print("2. Deleting a country")
        print("3. Search for a country")
        print("4. Editing the capital")
        print("5. Saving data")
        print("6. Loading data")
        print("0. Exit")

        choice = input("Make your choice: ")

        if choice == "1":
            country = input("Enter the name of the country: ")
            capital = input("Enter the name of the capital city: ")
            add_country(countries_data, country, capital)

        elif choice == "2":
            country = input("Enter the name of the country to delete: ")
            remove_country(countries_data, country)

        elif choice == "3":
            country = input("Enter the country name to search for: ")
            search_country(countries_data, country)

        elif choice == "4":
            country = input("Enter the name of the country to edit the capital: ")
            new_capital = input("Enter a new name for the capital: ")
            edit_country(countries_data, country, new_capital)

        elif choice == "5":
            save_data(countries_data, data_filename)
            print("Data saved.")

        elif choice == "6":
            countries_data = load_data(data_filename)
            print("Data loaded.")

        elif choice == "0":
            save_data(countries_data, data_filename)
            print("Thank you! \n Data saved.")
            break

        else:
            print("Try again.")
menu()
