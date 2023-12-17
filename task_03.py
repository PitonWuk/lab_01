"""
Завдання 3
До вже реалізованого класу «Дріб» додайте можливість стиснення та розпакування даних з
використанням json та pickle
"""
import json
import pickle

class Fraction:
    def __init__(self, numerator, denominator):
        self.numerator = numerator
        self.denominator = denominator

    def __str__(self):
        return f"{self.numerator}/{self.denominator}"

    def compress_json(self):
        data = {"numerator": self.numerator, "denominator": self.denominator}
        compressed_data = json.dumps(data)
        return compressed_data

    def decompress_json(self, compressed_data):
        data = json.loads(compressed_data)
        self.numerator = data["numerator"]
        self.denominator = data["denominator"]

    def compress_pickle(self):
        data = {"numerator": self.numerator, "denominator": self.denominator}
        compressed_data = pickle.dumps(data)
        return compressed_data

    def decompress_pickle(self, compressed_data):
        data = pickle.loads(compressed_data)
        self.numerator = data["numerator"]
        self.denominator = data["denominator"]


fraction = Fraction(3, 4)

compressed_json = fraction.compress_json()
print("Data compressed (JSON):", compressed_json)

fraction.decompress_json(compressed_json)
print("Uncompressed data (JSON):", fraction)

compressed_pickle = fraction.compress_pickle()
print("Data compressed (Pickle):", compressed_pickle)

fraction.decompress_pickle(compressed_pickle)
print("Uncompressed data (Pickle):", fraction)
