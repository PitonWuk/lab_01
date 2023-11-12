"""
Завдання 4
Створіть клас "Комп'ютер", який має зберігати
інформацію про процесор, ОЗУ та відеокарту. Застосуйте
інкапсуляцію для захисту цих даних від змін.
"""
class Computer:
    def __init__(self, processor, ram, graphics_card):
        self.__processor = processor
        self.__ram = ram
        self.__graphics_card = graphics_card

    def get_processor_info(self):
        return self.__processor

    def get_ram_info(self):
        return self.__ram

    def get_graphics_card_info(self):
        return self.__graphics_card

my_computer = Computer(processor="Ryzen 5", ram="16GB", graphics_card="NVIDIA GTX 960")

print("Processor:", my_computer.get_processor_info())
print("RAM:", my_computer.get_ram_info())
print("Graphics Card:", my_computer.get_graphics_card_info())