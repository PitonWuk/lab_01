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

