class ShoppingCart:
    def __init__(self):
        self.__items = {}

    def add_items(self, product, quantity, price):
        if product not in self.__items:
            self.__items[product] = {'quantity': quantity, 'price': price}
        else:
            self.__items[product]['quantity'] += quantity

    def calculate_total(self):
        total = 0
        for product, data in self.__items.items():
            total += data['quantity'] * data['price']
        return total

    def display_items(self):
        for product, data in self.__items.items():
            print(f"Product: {product} quantity {data['quantity']} ps price {data['price']}")


cart = ShoppingCart()
cart.add_items('Phone', 2, 100)
cart.add_items('Book', 3, 300)
cart.display_items()
print("Total price: ", cart.calculate_total())

