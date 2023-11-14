"""
Завдання 4
 Створіть клас InformationSystem, який має атрибут data
- словник, де ключі - це імена користувачів, а значення -
список їх контактів. Реалізуйте методи класу для додавання
нових користувачів та їх контактів.
"""
class InformationSystem:
    data = {}

    @classmethod
    def add_user(cls, username):
        if username not in cls.data:
            cls.data[username] = []

    @classmethod
    def add_contact(cls, username, contact):
        if username in cls.data:
            cls.data[username].append(contact)
        else:
            print(f"User {username} was not found.")

InformationSystem.add_user("Ivan")
InformationSystem.add_contact("Ivan", "123-45-67")

InformationSystem.add_user("Maria")
InformationSystem.add_contact("Maria", "987-65-43")

print(InformationSystem.data)

