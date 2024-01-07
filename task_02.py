"""
Завдання 2
Створіть імітаційну модель «Причал морських катерів».
Введіть таку інформацію:
1. Середній час між появою пасажирів на причалі у різний
час доби;
2. Середній час між появою катерів на причалі у різний час
доби;
3. Тип зупинки катера (кінцева або інша).
Визначіть:
1. Середній час перебування людини на зупинці;
2. Достатній інтервал часу між приходами катерів, коли на
зупинці не більше N людей одночасно;
3. Кількість вільних місць у катері є випадковою величиною.
Вибір необхідних структур даних визначте самостійно.
"""

import random
import time

class Passenger:
    def __init__(self, arrival_time):
        self.arrival_time = arrival_time
        self.stay_duration = random.uniform(5, 20)

class Boat:
    def __init__(self, arrival_time, stop_type):
        self.arrival_time = arrival_time
        self.stop_type = stop_type
        self.available_seats = random.randint(10, 30)

class DockSimulation:
    def __init__(self):
        self.passengers = []
        self.boats = []

    def generate_passengers(self, num_passengers):
        for _ in range(num_passengers):
            arrival_time = random.uniform(0, 24)
            passenger = Passenger(arrival_time)
            self.passengers.append(passenger)

    def generate_boats(self, num_boats):
        for _ in range(num_boats):
            arrival_time = random.uniform(0, 24)
            stop_type = random.choice(["end", "other"])
            boat = Boat(arrival_time, stop_type)
            self.boats.append(boat)

    def simulate_dock(self):
        for boat in self.boats:
            print(f"Boat arrived at {boat.arrival_time} with {boat.available_seats} available seats and {boat.stop_type} stop.")

            passengers_at_stop = [p for p in self.passengers if p.arrival_time <= boat.arrival_time]
            passengers_in_boat = []

            for passenger in passengers_at_stop:
                if passenger.stay_duration > 0 and (boat.stop_type == "other" or boat.available_seats > 0):
                    passengers_in_boat.append(passenger)
                    passenger.stay_duration -= 1
                    if boat.stop_type == "other":
                        boat.available_seats -= 1

            self.passengers = [p for p in self.passengers if p not in passengers_in_boat]

            print(f"Passengers boarded: {len(passengers_in_boat)}, Available seats after boarding: {boat.available_seats}")


dock_simulator = DockSimulation()
dock_simulator.generate_passengers(50)
dock_simulator.generate_boats(10)

for _ in range(24):
    dock_simulator.simulate_dock()
    time.sleep(1)
