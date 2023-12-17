"""
Завдання 1
Створіть два окремих "мікросервіси" (дві окремі
програми). Одна програма створює та експортує дані у
форматі JSON, а інша програма завантажує та обробляє ці
дані. Це може бути, наприклад, система, яка створює та
обробляє замовлення.

"""
import json

class OrderCreator:
    def create_order(self, order_id, product, quantity, price):
        order_data = {
            "order_id": order_id,
            "product": product,
            "quantity": quantity,
            "price": price
        }
        return order_data

    def export_order_to_json(self, order_data, filename):
        with open(filename, "w") as file:
            json.dump(order_data, file, indent=2)


order_creator = OrderCreator()
new_order = order_creator.create_order(order_id=1, product="Laptop", quantity=2, price=1200)
order_creator.export_order_to_json(new_order, "order1.json")
