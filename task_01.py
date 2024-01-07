"""
Завдання 1
Реалізуйте базу даних зі штрафами податкової
інспекції. Ідентифікувати кожну конкретну людину буде
персональний ідентифікаційний код. В однієї людини може
бути багато штрафів.
Реалізуйте:
1. Повний друк бази даних;
2. Друк даних за конкретним кодом;
3. Друк даних за конкретним типом штрафу;
4. Друк даних за конкретним містом;
5. Додавання нової людини з інформацією про неї;
6. Додавання нових штрафів для вже існуючого запису;
7. Видалення штрафу;
8. Заміна інформації про людину та її штрафи.
Використайте дерево для реалізації цього завдання.
"""
class Penalty:
    def __init__(self, penalty_type, city):
        self.penalty_type = penalty_type
        self.city = city

class Person:
    def __init__(self, personal_id, name, penalties=None):
        self.personal_id = personal_id
        self.name = name
        self.penalties = penalties or []

class PenaltyDatabaseNode:
    def __init__(self, data=None):
        self.data = data
        self.children = {}

class PenaltyDatabase:
    def __init__(self):
        self.root = PenaltyDatabaseNode()

    def add_person(self, person):
        node = self.root
        for digit in person.personal_id:
            if digit not in node.children:
                node.children[digit] = PenaltyDatabaseNode()
            node = node.children[digit]
        node.data = person

    def add_penalty(self, personal_id, penalty):
        node = self.find_node_by_id(personal_id)
        if node:
            node.data.penalties.append(penalty)

    def find_node_by_id(self, personal_id):
        node = self.root
        for digit in personal_id:
            if digit not in node.children:
                return None
            node = node.children[digit]
        return node

    def print_database(self, node=None):
        node = node or self.root
        if node.data:
            print(f"Person: {node.data.name}, ID: {node.data.personal_id}")
            for penalty in node.data.penalties:
                print(f"  Penalty: {penalty.penalty_type}, City: {penalty.city}")
        for child_node in node.children.values():
            self.print_database(child_node)

    def print_data_by_id(self, personal_id):
        node = self.find_node_by_id(personal_id)
        if node and node.data:
            print(f"Person: {node.data.name}, ID: {node.data.personal_id}")
            for penalty in node.data.penalties:
                print(f"  Penalty: {penalty.penalty_type}, City: {penalty.city}")
        else:
            print(f"Person with ID {personal_id} not found.")

    def print_data_by_penalty_type(self, penalty_type):
        self._print_data_by_condition(lambda person: any(p.penalty_type == penalty_type for p in person.penalties),
                                       f"People with Penalty Type: {penalty_type}")

    def print_data_by_city(self, city):
        self._print_data_by_condition(lambda person: any(p.city == city for p in person.penalties),
                                       f"People with Penalty in City: {city}")

    def _print_data_by_condition(self, condition, header):
        def print_person_data(person):
            print(f"Person: {person.name}, ID: {person.personal_id}")
            for penalty in person.penalties:
                print(f"  Penalty: {penalty.penalty_type}, City: {penalty.city}")

        print(header)
        self._traverse_and_print(self.root, condition, print_person_data)

    def _traverse_and_print(self, node, condition, print_func):
        if node.data and condition(node.data):
            print_func(node.data)
        for child_node in node.children.values():
            self._traverse_and_print(child_node, condition, print_func)

penalty_db = PenaltyDatabase()

person1 = Person("1234567890", "John Doe")
penalty1 = Penalty("Speeding", "New York")
penalty_db.add_person(person1)
penalty_db.add_penalty(person1.personal_id, penalty1)


penalty_db.print_database()

penalty_db.print_data_by_id("1234567890")

penalty_db.print_data_by_penalty_type("Speeding")

penalty_db.print_data_by_city("New York")
