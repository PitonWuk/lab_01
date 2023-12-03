"""
Завдання 1
Іноді ви можете використати property() для створення
доступу до атрибутів через геттери та сеттери для
забезпечення певних перевірок або операцій перед
отриманням або зміною атрибутів. Створіть клас для
роботи з банківським рахунком, щоб гроші знялися або
зарахувалися тільки при виконанні певних умов
(наприклад, якщо гроші на рахунку є).
"""
class BankAccount:
    def __init__(self, balance=0):
        self._balance = balance

    @property
    def balance(self):
        return self._balance

    @balance.setter
    def balance(self, amount):
        if amount < 0:
            print("The amount must be positive.")
        else:
            self._balance = amount
            print(f"Balance updated: {amount}")

    def deposit(self, amount):
        self.balance += amount

    def withdraw(self, amount):
        if amount > self.balance:
            print("Not enough money")
        else:
            self.balance -= amount
            print(f"Withdrawn {amount} . Balance: {self.balance}")


account = BankAccount(1000)
print(f"Opening balance sheet: {account.balance}.")

account.withdraw(500)
account.deposit(200)
account.balance = 1500

print(f"Final balance sheet: {account.balance}.")
