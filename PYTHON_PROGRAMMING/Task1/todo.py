"""
To-Do List Application
CodSoft Python Programming Internship - Task 1

A command-line To-Do List manager that lets a user create, view, update,
mark-complete, and delete tasks. Tasks are stored persistently in a local
JSON file (data/tasks.json) so they survive between runs.
"""

import json
import os
from datetime import datetime

DATA_DIR = os.path.join(os.path.dirname(os.path.abspath(__file__)), "data")
DATA_FILE = os.path.join(DATA_DIR, "tasks.json")


def ensure_data_file():
    """Create the data folder/file the first time the app runs."""
    os.makedirs(DATA_DIR, exist_ok=True)
    if not os.path.exists(DATA_FILE):
        with open(DATA_FILE, "w") as f:
            json.dump([], f)


def load_tasks():
    ensure_data_file()
    with open(DATA_FILE, "r") as f:
        return json.load(f)


def save_tasks(tasks):
    with open(DATA_FILE, "w") as f:
        json.dump(tasks, f, indent=4)


def add_task(tasks):
    title = input("Enter task title: ").strip()
    if not title:
        print("Task title cannot be empty.\n")
        return
    description = input("Enter task description (optional): ").strip()
    task = {
        "id": (max([t["id"] for t in tasks], default=0) + 1),
        "title": title,
        "description": description,
        "done": False,
        "created_at": datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
    }
    tasks.append(task)
    save_tasks(tasks)
    print(f"Task '{title}' added successfully.\n")


def view_tasks(tasks):
    if not tasks:
        print("No tasks yet. Add one to get started!\n")
        return
    print("\n" + "-" * 50)
    print(f"{'ID':<4}{'Status':<8}{'Title':<25}")
    print("-" * 50)
    for t in tasks:
        status = "[X]" if t["done"] else "[ ]"
        print(f"{t['id']:<4}{status:<8}{t['title']:<25}")
        if t.get("description"):
            print(f"      -> {t['description']}")
    print("-" * 50 + "\n")


def update_task(tasks):
    view_tasks(tasks)
    if not tasks:
        return
    try:
        task_id = int(input("Enter the ID of the task to update: "))
    except ValueError:
        print("Please enter a valid numeric ID.\n")
        return
    for t in tasks:
        if t["id"] == task_id:
            new_title = input(f"New title (leave blank to keep '{t['title']}'): ").strip()
            new_desc = input("New description (leave blank to keep current): ").strip()
            if new_title:
                t["title"] = new_title
            if new_desc:
                t["description"] = new_desc
            save_tasks(tasks)
            print("Task updated successfully.\n")
            return
    print("Task ID not found.\n")


def mark_complete(tasks):
    view_tasks(tasks)
    if not tasks:
        return
    try:
        task_id = int(input("Enter the ID of the task to mark complete: "))
    except ValueError:
        print("Please enter a valid numeric ID.\n")
        return
    for t in tasks:
        if t["id"] == task_id:
            t["done"] = True
            save_tasks(tasks)
            print("Task marked as complete.\n")
            return
    print("Task ID not found.\n")


def delete_task(tasks):
    view_tasks(tasks)
    if not tasks:
        return
    try:
        task_id = int(input("Enter the ID of the task to delete: "))
    except ValueError:
        print("Please enter a valid numeric ID.\n")
        return
    for t in tasks:
        if t["id"] == task_id:
            tasks.remove(t)
            save_tasks(tasks)
            print("Task deleted successfully.\n")
            return
    print("Task ID not found.\n")


def print_menu():
    print("=" * 50)
    print("            TO-DO LIST APPLICATION")
    print("=" * 50)
    print("1. Add Task")
    print("2. View Tasks")
    print("3. Update Task")
    print("4. Mark Task as Complete")
    print("5. Delete Task")
    print("6. Exit")
    print("=" * 50)


def main():
    tasks = load_tasks()
    while True:
        print_menu()
        choice = input("Choose an option (1-6): ").strip()
        if choice == "1":
            add_task(tasks)
        elif choice == "2":
            view_tasks(tasks)
        elif choice == "3":
            update_task(tasks)
        elif choice == "4":
            mark_complete(tasks)
        elif choice == "5":
            delete_task(tasks)
        elif choice == "6":
            print("Goodbye!")
            break
        else:
            print("Invalid choice. Please select 1-6.\n")


if __name__ == "__main__":
    main()
