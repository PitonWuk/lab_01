"""
Завдання 2
Створіть клас Passport (паспорт), який міститиме
паспортну інформацію про громадянина заданої країни.
За допомогою механізму успадкування реалізуйте
клас ForeignPassport (закордонний паспорт), похідний
від Passport.
Нагадаємо, що закордонний паспорт містить, крім
паспортних даних, дані про візи і номер закордонного
паспорта.
Кожен із класів має містити необхідні методи.
"""

class Passport:
    def __init__(self, series, number, full_name):
        self.series = series
        self.number = number
        self.full_name = full_name

    def dispay_info(self):
        print(f"Passport information: \nSeries: {self.series}\nNumber: {self.number}\nFull name: {self.full_name}")

class ForeignPassport(Passport):
    def __init__(self, series, number, full_name, name_visa, passport_number):
        super().__init__(series, number, full_name)
        self.name_visa = name_visa
        self.passport_number = passport_number

    def dispay_info(self):
        super().dispay_info()
        print(f"Foreign Passport Information:\nVisa Info: {self.name_visa}\nForeign Passport Number: {self.passport_number}")

passport = Passport("KA", 231252, "Full Name")
passport.dispay_info()

print("\n")
foreign_passprot = ForeignPassport("KA", 231252, "Full Name", "USA", 215452)
foreign_passprot.dispay_info()
