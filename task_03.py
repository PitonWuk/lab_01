"""
Завдання 3
До вже реалізованого класу «Стадіон» додайте можливість
стиснення та розпакування даних з використанням json та
pickle.

"""
import json
import pickle

class Stadium:
    def __init__(self, name, capacity, location):
        self.name = name
        self.capacity = capacity
        self.location = location

    def __str__(self):
        return f"{self.name} (Capacity: {self.capacity}, Location: {self.location})"

    def compress_json(self):
        data = {
            "name": self.name,
            "capacity": self.capacity,
            "location": self.location
        }
        compressed_data = json.dumps(data)
        return compressed_data

    def decompress_json(self, compressed_data):
        data = json.loads(compressed_data)
        self.name = data["name"]
        self.capacity = data["capacity"]
        self.location = data["location"]

    def compress_pickle(self):
        data = {
            "name": self.name,
            "capacity": self.capacity,
            "location": self.location
        }
        compressed_data = pickle.dumps(data)
        return compressed_data

    def decompress_pickle(self, compressed_data):
        data = pickle.loads(compressed_data)
        self.name = data["name"]
        self.capacity = data["capacity"]
        self.location = data["location"]


stadium = Stadium(name="Camp Nou", capacity=99000, location="Barcelona")

compressed_json = stadium.compress_json()
print("Compressed data (JSON):", compressed_json)

stadium.decompress_json(compressed_json)
print("Uncompressed data (JSON):", stadium)

compressed_pickle = stadium.compress_pickle()
print("Compressed data (Pickle):", compressed_pickle)

stadium.decompress_pickle(compressed_pickle)
print("Uncompressed data (Pickle):", stadium)