"""
Завдання 3
Створіть клас для представлення відомостей про
замовлення. Забезпечте, щоб номер замовлення був
тільки для читання за допомогою керованих атрибутів,
але його можна було переглядати.
"""
class Order:
    def __init__(self, order_number, customer_name, total_amount):
        self._order_number = order_number
        self.customer_name = customer_name
        self.total_amount = total_amount

    @property
    def order_number(self):
        return self._order_number

order = Order(order_number="ORD123", customer_name="John Doe", total_amount=100.00)

print("Order number:", order.order_number)

try:
    order.order_number = "ORD456"
except AttributeError as e:
    print(f"Error: {e}")
