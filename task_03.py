"""
Завдання 3
Створіть клас для конвертування з метричної системи в
англійську, та навпаки. Реалізуйте функціональність у вигляді
статичних методів. Обов’язково реалізуйте конвертування
заходів довжини.
"""
class LengthConverter:
    count = 0

    @staticmethod
    def from_meters_to_feet(length_in_meters):
        LengthConverter.count += 1
        return length_in_meters * 3.28084

    @staticmethod
    def from_feet_to_meters(length_in_feet):
        LengthConverter.count += 1
        return length_in_feet / 3.28084

    @staticmethod
    def number_of_counts_of_length():
        return LengthConverter.count

length_in_meters = 10
length_in_feet = LengthConverter.from_meters_to_feet(length_in_meters)
print(f"{length_in_meters} meters = {length_in_feet} feet")

print(f"Number of length counts: {LengthConverter.number_of_counts_of_length()}")

