"""
Завдання 3
Створіть клас "Електронний Гаманець" додавши
можливість видаляти та додавати гроші, а також перевіряти
баланс.
"""
class ElectronicWallet:
    def __init__(self, balance=0):
        self.__balance = balance

    def add_money(self, amount):
        if amount > 0:
            self.__balance += amount
            print(f"Added {amount} to the wallet. New balance: {self.__balance}")
        else:
            print("Invalid amount. Please add a positive value.")

    def remove_money(self, amount):
        if amount > 0 and amount <= self.__balance:
            self.__balance -= amount
            print(f"Removed {amount} from the wallet. New balance: {self.__balance}")
        elif amount <= 0:
            print("Invalid amount. Please enter a positive value.")
        else:
            print("Insufficient funds.")

    def check_balance(self):
        print(f"Current balance: {self.__balance}")

# Example usage:
wallet = ElectronicWallet()

wallet.add_money(55)
wallet.check_balance()

wallet.remove_money(18)
wallet.check_balance()

wallet.remove_money(35)