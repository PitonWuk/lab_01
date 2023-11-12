"""
Завдання 2
Розробіть систему управління замовленнями таксі.
Кожне замовлення має містити інформацію про
клієнта, адресу, тип автомобіля та вартість. Реалізуйте
методи для додавання нових замовлень, зміни адреси та
типу автомобіля, а також видалення замовлення.
Використайте інкапсуляцію для захисту вартості від
неправильних змін.
"""
class TaxiOrderManagementSystem:
    def __init__(self):
        self._orders = []

    def add_order(self, client, address, car_type, cost):
        order = {
            "client": client,
            "address": address,
            "car_type": car_type,
            "cost": cost
        }
        self._orders.append(order)
        print("New order added.")

    def update_order(self, order_id, new_address, new_car_type):

        for order in self._orders:
            if order.get("order_id") == order_id:

                if new_address:
                    order["address"] = new_address
                if new_car_type:
                    order["car_type"] = new_car_type
                print(f"Order {order_id} updated.")
                break
        else:
            print(f"Order with ID {order_id} not found.")

    def remove_order(self, order_id):

        order_to_remove = None
        for order in self._orders:
            if order.get("order_id") == order_id:
                order_to_remove = order
                break


        if order_to_remove:
            self._orders.remove(order_to_remove)
            print(f"Order with ID {order_id} has been removed.")
        else:
            print(f"Order with ID {order_id} not found.")

taxi_system = TaxiOrderManagementSystem()
taxi_system.add_order("John Doe", "123 Main St", "Sedan", 25.0)
taxi_system.add_order("Jane Smith", "456 Oak St", "SUV", 40.0)

taxi_system.update_order(1, new_address="789 Elm St", new_car_type="Van")
taxi_system.remove_order(2)