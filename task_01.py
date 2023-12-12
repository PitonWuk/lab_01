"""
Завдання 1
Користувач заповнює з клавіатури список цілих.
Стисніть отримані дані та збережіть їх у файл. Після цього
завантажте дані з файлу в новий список.

"""
import pickle
import gzip

def compressed_data(data, filename):
    with gzip.open(filename, 'wb') as file:
        pickle.dump(data, file)

def load_data(filename):
    with gzip.open(filename, 'rb') as file:
        loaded_data = pickle.load(file)
    return loaded_data

user_numbers = input("Enter the list of integer numbers using space: ")
user_list = [int(x) for x in user_numbers.split()]

filename = "compressed_data.gz"

compressed_data(user_list, filename)
loaded_list = load_data(filename)

