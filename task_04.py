"""
Завдання 4
Створіть базовий клас Clock, який містить атрибути
години та хвилини. Від цього базового класу
успадковуйте два класи: AnalogClock та DigitalClock.
Клас AnalogClock повинен мати метод display_time,
який виводить поточний час у форматі
"години:хвилини". Клас DigitalClock повинен мати
метод display_time, який виводить поточний час у
цифровому форматі "гг:хх".
Створіть об'єкти кожного класу та виведіть
поточний час за допомогою методу display_time.

"""
from datetime import datetime

class Clock:
    def __init__(self, hours, minutes):
        self.hours = hours
        self.minutes = minutes

class AnalogClock(Clock):
    def display_time(self):
        print(f"{self.hours:02d} hours and {self.minutes:02d} minutes")

class DigitalClock(Clock):
    def display_time(self):
        print(f"{self.hours:02d}:{self.minutes:02d}")

now = datetime.now()
current_hours = now.hour
current_minutes = now.minute

analog_clock = AnalogClock(hours=current_hours, minutes=current_minutes)
digital_clock = DigitalClock(hours=current_hours, minutes=current_minutes)

print("Analog Clock:")
analog_clock.display_time()

print("\nDigital Clock:")
digital_clock.display_time()