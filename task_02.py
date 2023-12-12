"""
Завдання 2
Маємо певний словник з назвами музичних груп (виконавців) та альбомів. Назва групи використовується як ключ,
назва альбомів — як значення. Реалізуйте: додавання, видалення, пошук, редагування, збереження та завантаження
даних (використовуючи стиснення та розпакування).
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

def add_group(data, group, albums):
    data[group] = albums
    print(f"Added: {group} — {albums}.")

def remove_group(data, group):
    if group in data:
        del data[group]
        print(f"Deleted: {group}.")
    else:
        print(f"Group {group} did not found.")

def search_group(data, group):
    if group in data:
        print(f"{group} — {data[group]}.")
    else:
        print(f"Group {group} did not found.")

def edit_group(data, group, new_albums):
    if group in data:
        data[group] = new_albums
        print(f"Edited: {group} — {new_albums}.")
    else:
        print(f"Group {group} did not found.")

def menu():
    data_filename = "music_data.gz"
    music_data = load_data(data_filename)

    while True:
        print("\nMenu:")
        print("1. Add a group")
        print("2. Delete a group")
        print("3. Search for a group")
        print("4. Edit albums")
        print("5. Saving data")
        print("6. Loading data")
        print("0. Exit")

        choice = input("Make your choice: ")

        if choice == "1":
            group = input("Enter the name of the group: ")
            albums = input("Enter the name of the album (separated by commas if there is more than one): ")
            add_group(music_data, group, albums)

        elif choice == "2":
            group = input("Enter the name of the group to delete: ")
            remove_group(music_data, group)

        elif choice == "3":
            group = input("Enter the name of the group to search for: ")
            search_group(music_data, group)

        elif choice == "4":
            group = input("Enter a group name to edit albums: ")
            new_albums = input("Enter a new album name (separated by commas if there is more than one): ")
            edit_group(music_data, group, new_albums)

        elif choice == "5":
            save_data(music_data, data_filename)
            print("Data saved.")

        elif choice == "6":
            music_data = load_data(data_filename)
            print("Data loaded.")

        elif choice == "0":
            save_data(music_data, data_filename)
            print("Thank you. \n Data saved.")
            break

        else:
            print("Try again.")

menu()

