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
class Clock:
    def __init__(self, hours, minutes):
        self.hours = hours
        self.minutes = minutes

    def display_times(self):
        super().display_times()
        #print(f"{self.hours:02d}:{self.minutes:02d}")


class AnalogClock(Clock):
    pass

analog_clock = AnalogClock(1, 45)
analog_clock.display_times()