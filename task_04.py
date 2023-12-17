"""
До вже реалізованого класу «Годинник» додайте
мож-ливість стиснення та розпакування даних з
використан-ням json та pickle.

"""
import json
import pickle

class Clock:
    def __init__(self, hours, minutes, seconds):
        self.hours = hours
        self.minutes = minutes
        self.seconds = seconds

    def __str__(self):
        return f"{self.hours:02d}:{self.minutes:02d}:{self.seconds:02d}"

    def compress_json(self):
        data = {"hours": self.hours, "minutes": self.minutes, "seconds": self.seconds}
        compressed_data = json.dumps(data)
        return compressed_data

    def decompress_json(self, compressed_data):
        data = json.loads(compressed_data)
        self.hours = data["hours"]
        self.minutes = data["minutes"]
        self.seconds = data["seconds"]

    def compress_pickle(self):
        data = {"hours": self.hours, "minutes": self.minutes, "seconds": self.seconds}
        compressed_data = pickle.dumps(data)
        return compressed_data

    def decompress_pickle(self, compressed_data):
        data = pickle.loads(compressed_data)
        self.hours = data["hours"]
        self.minutes = data["minutes"]
        self.seconds = data["seconds"]

clock = Clock(12, 30, 45)

compressed_json = clock.compress_json()
print("Compressed data (JSON):", compressed_json)

clock.decompress_json(compressed_json)
print("Uncompressed data (JSON):", clock)

compressed_pickle = clock.compress_pickle()
print("Compressed data (Pickle):", compressed_pickle)

clock.decompress_pickle(compressed_pickle)
print("Uncompressed data (Pickle):", clock)
