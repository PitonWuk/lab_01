"""
Завдання 2
Створіть клас температурного датчика, де обмежується
температура в межах прийнятних для датчика значень, за
допомогою property().
"""
class TemperatureSensor:
    def __init__(self):
        self._temperature = 0

    @property
    def temperature(self):
        return self._temperature

    @temperature.setter
    def temperature(self, value):
        if -50 <= value <= 50:
            self._temperature = value
        else:
            print("Unacceptable temperature. Set a value between -50 and 50 degrees Celsius.")

sensor = TemperatureSensor()

sensor.temperature = 25
sensor.temperature = 60

print(f"Temperature: {sensor.temperature} degrees Celsius")