"""
Завдання 3
Маємо певний словник з логінами і паролями користувачів. Логін використовується як ключ, пароль —
як значення. Реалізуйте: додавання, видалення, пошук,
редагування, збереження та завантаження даних (використовуючи стиснення та розпакування).
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

def add_user(data, login, password):
    if login not in data:
        data[login] = password
        print(f"User {login} added with password {password}.")
    else:
        print(f"User with login {login} already exists.")

def remove_user(data, login):
    if login in data:
        del data[login]
        print(f"User {login} deleted.")
    else:
        print(f"User with login {login} did not found.")

def search_user(data, login):
    if login in data:
        print(f"User with login {login} found, password: {data[login]}.")
    else:
        print(f"User with login {login} did not found.")

def edit_user(data, login, new_password):
    if login in data:
        data[login] = new_password
        print(f"Password for user {login} edited.")
    else:
        print(f"User with login {login} dai not found.")

def menu():
    data_filename = "user_data.gz"
    user_data = load_data(data_filename)

    while True:
        print("\nMenu:")
        print("1. Adding a user")
        print("2. Deleting a user")
        print("3. Search for a user")
        print("4. Edit password")
        print("5. Saving data")
        print("6. Loading data")
        print("0. Exit")

        choice = input("Make your choice: ")

        if choice == "1":
            login = input("Enter login: ")
            password = input("Enter password: ")
            add_user(user_data, login, password)

        elif choice == "2":
            login = input("Enter your login to delete: ")
            remove_user(user_data, login)

        elif choice == "3":
            login = input("Enter your login to search: ")
            search_user(user_data, login)

        elif choice == "4":
            login = input("Enter your login to edit your password: ")
            new_password = input("Enter a new password: ")
            edit_user(user_data, login, new_password)

        elif choice == "5":
            save_data(user_data, data_filename)
            print("Data saved.")

        elif choice == "6":
            user_data = load_data(data_filename)
            print("Data loaded.")

        elif choice == "0":
            save_data(user_data, data_filename)
            print("Thank you. \nData saved.")
            break

        else:
            print("Tray again.")

menu()

