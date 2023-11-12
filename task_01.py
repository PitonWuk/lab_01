"""
Завдання 1
Створіть систему управління замовленнями
готелю. Кожне замовлення має містити інформацію
про клієнта, тип кімнати, кількість днів проживання та
вартість. Реалізуйте методи для додавання замовлення,
зміни типу кімнати та кількості днів, а також
видалення замовлення. Використайте інкапсуляцію для
захисту вартості від неправильних змін.
"""
class HotelManagementSystem:
    def __init__(self, order_id, client_name, room_type, num_days, cost_per_day):
        self._order_id = order_id
        self._client_name = client_name
        self._room_type = room_type
        self._num_days = num_days
        self._cost_per_day = cost_per_day
        self._total_cost = self._calculate_total_cost()
        self._orders = []

    def _calculate_total_cost(self):
        return self._num_days * self._cost_per_day

    def get_client_name(self):
        return self._client_name

    def get_room_type(self):
        return self._room_type

    def get_num_days(self):
        return self._num_days

    def get_total_cost(self):
        return self._total_cost

    def update_room_type(self, new_room_type):
        self._room_type = new_room_type
        self._total_cost = self._calculate_total_cost()

    def update_num_days(self, new_num_days):
        self._num_days = new_num_days
        self._total_cost = self._calculate_total_cost()

    def remove_order(self, order_id):
        order_to_remove = None
        for order in self._orders:
            if order["order_id"] == order_id:
                order_to_remove = order
                break

        if order_to_remove:
            self._orders.remove(order_to_remove)
            print(f"Order with ID {order_id} has been removed.")
        else:
            print(f"Order with ID {order_id} not found.")



hotel_system = HotelManagementSystem(order_id = 4, client_name="John Doe", room_type="Single", num_days=3, cost_per_day=50)
hotel_system.orders = [
    {"order_id": 1, "client": "John Doe", "room_type": "single", "days": 3, "cost": 150},
    {"order_id": 2, "client": "Jane Doe", "room_type": "double", "days": 5, "cost": 250},
    {"order_id": 3, "client": "Bob Smith", "room_type": "suite", "days": 7, "cost": 400},
]
print("Client:", hotel_system.get_client_name())
print("Room Type:", hotel_system.get_room_type())
print("Number of Days:", hotel_system.get_num_days())
print("Total Cost:", hotel_system.get_total_cost())

hotel_system.update_room_type("Double")
hotel_system.update_num_days(5)

print("Updated Room Type:", hotel_system.get_room_type())
print("Updated Number of Days:", hotel_system.get_num_days())
print("Updated Total Cost:", hotel_system.get_total_cost())

hotel_system.remove_order(3)