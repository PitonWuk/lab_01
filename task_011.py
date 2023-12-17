import json

class OrderProcessor:
    def load_order_from_json(self, filename):
        try:
            with open(filename, "r") as file:
                order_data = json.load(file)
            return order_data
        except FileNotFoundError:
            print(f"File {filename} not found.")
            return None

    def process_order(self, order_data):
        if order_data:
            print("Order processing:")
            for key, value in order_data.items():
                print(f"{key}: {value}")
        else:
            print("Order did not find.")


order_processor = OrderProcessor()
loaded_order = order_processor.load_order_from_json("order1.json")
order_processor.process_order(loaded_order)