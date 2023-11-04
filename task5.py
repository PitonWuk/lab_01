"""
Завдання 5
Створіть клас BankAccount з атрибутами balance
та owner, а також методами deposit та withdraw для
здійснення операцій з балансом. Реалізуйте перевірку
на те, що баланс не може стати від'ємним.
"""
class BankAccount:
    def __init__(self, owner, balance=0):
        self.balance = balance
        self.owner = owner

    def deposit(self, amount):
        if amount > 0:
            self.balance += amount
            print(f"Your balance is: {self.balance}")
        else:
            print(f"Amount is wrong.")

    def withdraw(self, amount):
        if amount > 0 and amount <= self.balance:
            self.balance -= amount
            print(f"Your withdraw: {amount}. Now your balance is: {self.balance}")

        elif amount < 0:
            print("Amount is wrong.")
        else:
            print("Not enough money on your deposit.")

money = BankAccount("Mark", 1000)
money.deposit(500)
money.withdraw(300)

money.withdraw(3000)





