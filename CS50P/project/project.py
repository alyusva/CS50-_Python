import json
from datetime import datetime

def main():
    while True:
        print("\nTask Manager")
        print("1. Add Task")
        print("2. Delete Task")
        print("3. View Tasks")
        print("4. Mark Task as Completed")
        print("5. Exit")
        choice = input("Choose an option: ")

        if choice == "1":
            description = input("Enter task description: ")
            due_date = input("Enter due date (YYYY-MM-DD): ")
            add_task(description, due_date)
        elif choice == "2":
            task_id = int(input("Enter task ID to delete: "))
            delete_task(task_id)
        elif choice == "3":
            view_tasks()
        elif choice == "4":
            task_id = int(input("Enter task ID to mark as completed: "))
            mark_task_as_completed(task_id)
        elif choice == "5":
            break
        else:
            print("Invalid choice. Please try again.")

def add_task(description, due_date):
    task = {"description": description, "due_date": due_date, "completed": False}

    tasks = load_tasks()
    tasks.append(task)
    save_tasks(tasks)
    print("Task added.")

def delete_task(task_id):
    tasks = load_tasks()
    if 0 <= task_id < len(tasks):
        tasks.pop(task_id)
        save_tasks(tasks)
        print("Task deleted.")
    else:
        print("Invalid task ID.")

def view_tasks():
    tasks = load_tasks()
    for i, task in enumerate(tasks):
        status = "Completed" if task["completed"] else "Pending"
        print(f"{i}. {task['description']} - Due: {task['due_date']} - Status: {status}")

def mark_task_as_completed(task_id):
    tasks = load_tasks()
    if 0 <= task_id < len(tasks):
        tasks[task_id]["completed"] = True
        save_tasks(tasks)
        print("Task marked as completed.")
    else:
        print("Invalid task ID.")

def load_tasks():
    try:
        with open("tasks.json", "r") as file:
            return json.load(file)
    except FileNotFoundError:
        return []

def save_tasks(tasks):
    with open("tasks.json", "w") as file:
        json.dump(tasks, file, indent=4)

if __name__ == "__main__":
    main()
