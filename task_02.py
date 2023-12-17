"""
Завдання 2
Реалізація програми для додавання, видалення та
відстеження завдань/заміток. Зберігати ці завдання у
форматі JSON у файлі. Можливість завантаження
раніше збережених завдань для подальшої роботи з
ними.
"""
import json
import os
import datetime

task_file = "tasks.json"

def load_tasks():
    try:
        with open(task_file, "r") as file:
            tasks = json.load(file)
        return tasks
    except FileNotFoundError:
        return []

def save_tasks(tasks):
    with open(task_file, "w") as file:
        json.dump(tasks, file, indent=2)

def display_tasks(tasks):
    if not tasks:
        print("No tasks.")
    else:
        print("List of tasks:")
        for index, task in enumerate(tasks, start=1):
            print(f"{index}. {task}")

def add_task(tasks, new_task):
    tasks.append(new_task)
    save_tasks(tasks)
    print(f"Added new task: {new_task}")

def remove_task(tasks, index):
    if 1 <= index <= len(tasks):
        removed_task = tasks.pop(index - 1)
        save_tasks(tasks)
        print(f"Deleted task: {removed_task}")
    else:
        print("Try again.")

def menu():
    tasks = load_tasks()

    while True:
        print("\nMenu:")
        print("1. Display the list of tasks")
        print("2. Add a new task")
        print("3. Delete a task")
        print("4. Exit")

        choice = input("Make your choice: ")

        if choice == "1":
            display_tasks(tasks)

        elif choice == "2":
            new_task = input("Enter a new task: ")
            add_task(tasks, new_task)

        elif choice == "3":
            display_tasks(tasks)
            index_to_remove = int(input("Enter the task number to delete: "))
            remove_task(tasks, index_to_remove)

        elif choice == "4":
            print("Thank you!.")
            break

        else:
            print("Try again.")
menu()
