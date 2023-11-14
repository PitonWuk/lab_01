"""
Завдання 2
Створіть клас для конвертування температури з Цельсія
у Фаренгейт, і навпаки. У класі має знаходитися два статичні
методи: для конвертування з Цельсія у Фаренгейт і для конвертування з Фаренгейта у Цельсій. Також клас має розрахувати
кількість підрахунків температури та повернути це значення
статичним методом.
"""
class Convert:
    convert_count = 0

    @staticmethod
    def cels_to_fareng(cels):
        Convert.convert_count += 1
        return (cels * 9/5) + 32

    @staticmethod
    def farenf_to_cels(fareng):
        Convert.convert_count += 1
        return (fareng - 32) * 5 / 9

    @staticmethod
    def count_quantity():
        return Convert.convert_count

cels = 26
fareng = Convert.cels_to_fareng(cels)
print(fareng)

fareng = 12
cels = Convert.farenf_to_cels(fareng)
print(fareng)
print(f"Quantity: {Convert.convert_count}")
