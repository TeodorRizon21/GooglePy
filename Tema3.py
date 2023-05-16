import datetime
import json

categories = {}


tasks = []
def load_data():
    try:
        with open("categories.json", "r") as f:
            categories = json.load(f)
    except FileNotFoundError:
        categories = {}

    try:
        with open("tasks.json", "r") as f:
            tasks = json.load(f)
    except FileNotFoundError:
        tasks = []

    return categories, tasks


def save_data():
    with open("categories.json", "w") as f:
        json.dump(categories, f)

    with open("tasks.json", "w") as f:
        json.dump(tasks, f)


def add_category():
    category_name = input("Enter the name of the category: ")
    categories[category_name] = {}
    print(f"Category '{category_name}' added.")


def add_task():
    task_name = input("Enter the name of the task: ")
    deadline_str = input("Enter the deadline in format 'YYYY-MM-DD HH:MM': ")
    responsible_name = input("Enter the name of the responsible person: ")
    category_name = input("Enter the category name: ")

    if category_name not in categories:
        print(f"Error: category '{category_name}' does not exist.")
        return

    try:
        deadline = datetime.datetime.strptime(deadline_str, "%Y-%m-%d %H:%M")
    except ValueError:
        print("Error: deadline format is incorrect.")
        return

    task = {
        "name": task_name,
        "deadline": deadline.strftime("%Y-%m-%d %H:%M"),
        "responsible": responsible_name,
        "category": category_name
    }
    tasks.append(task)
    print(f"Task '{task_name}' added.")


def list_categories_and_tasks():
    if not categories:
        print("No categories found.")
    else:
        for category, tasks_dict in categories.items():
            print(f"{category}:")
            if not tasks_dict:
                print("  No tasks found.")
            else:
                for task_name in tasks_dict:
                    print(f"  - {task_name}")

    if not tasks:
        print("No tasks found.")
    else:
        print("All tasks:")
        for task in tasks:
            print(f"{task['name']} - {task['deadline']} - {task['responsible']} - {task['category']}")


def filter_tasks():
    search_str = input("Enter a string to search for: ")
    found_tasks = []
    for task in tasks:
        if search_str in task["name"] or search_str in task["responsible"]:
            found_tasks.append(task)
    if not found_tasks:
        print("No tasks found.")
    else:
        print(f"Tasks containing '{search_str}':")
        for task in found_tasks:
            print(f"{task['name']} - {task['deadline']} - {task['responsible']} - {task['category']}")


def edit_category():
    category_name = input("Enter the name of the category to edit: ")
    if category_name not in categories:
        print(f"Error: category '{category_name}' does not exist.")
        return
    new_name = input("Enter the new name for the category: ")

    categories[new_name] = categories.pop(category_name)

    for task in tasks:
        if task["category"] == category_name:
            task["category"] = new_name

    print(f"Category '{category_name}' edited to '{new_name}'.")


def edit_task():
    task_name = input("Enter the name of the task to edit: ")
    for task in tasks:
        if task["name"] == task_name:
            new_name = input("Enter the new name for the task: ")
            deadline_str = input("Enter the new deadline in format 'YYYY-MM-DD HH:MM': ")
            responsible_name = input("Enter the new name of the responsible person: ")
            category_name = input("Enter the new category name: ")

            if category_name not in categories:
                print(f"Error: category '{category_name}' does not exist.")
                return

            try:
                deadline = datetime.datetime.strptime(deadline_str, "%Y-%m-%d %H:%M")
            except ValueError:
                print("Error: deadline format is incorrect.")
                return

            task["name"] = new_name
            task["deadline"] = deadline.strftime("%Y-%m-%d %H:%M")
            task["responsible"] = responsible_name
            task["category"] = category_name

            print(f"Task '{task_name}' edited.")
            return

    print(f"Error: task '{task_name}' not found.")


def delete_category():
    category_name = input("Enter the name of the category to delete: ")
    if category_name not in categories:
        print(f"Error: category '{category_name}' does not exist.")
        return
    categories.pop(category_name)

    tasks_to_delete = []
    for task in tasks:
        if task["category"] == category_name:
            tasks_to_delete.append(task)
    for task in tasks_to_delete:
        tasks.remove(task)

    print(f"Category '{category_name}' deleted.")


def delete_task():
    task_name = input("Enter the name of the task to delete: ")
    for task in tasks:
        if task["name"] == task_name:
            tasks.remove(task)
            print(f"Task '{task_name}' deleted.")
            return

    print(f"Error: task '{task_name}' not found.")


def sort_tasks_by_name(reverse=False):
    tasks.sort(key=lambda x: x["name"], reverse=reverse)
    print("Tasks sorted by name:" if not reverse else "Tasks sorted by name in reverse order:")
    for task in tasks:
        print(f"{task['name']} - {task['deadline']} - {task['responsible']} - {task['category']}")


def sort_tasks_by_date(reverse=False):
    tasks.sort(key=lambda x: x["deadline"], reverse=reverse)
    print("Tasks sorted by date:" if not reverse else "Tasks sorted by date in reverse order:")
    for task in tasks:
        print(f"{task['name']} - {task['deadline']} - {task['responsible']} - {task['category']}")


def sort_tasks_by_responsible(reverse=False):
    tasks.sort(key=lambda x: x["responsible"], reverse=reverse)
    print(
        "Tasks sorted by responsible person:" if not reverse else "Tasks sorted by responsible person in reverse order:")

    for task in tasks:
        print(f"{task['name']} - {task['deadline']} - {task['responsible']} - {task['category']}")


def sort_tasks_by_category(reverse=False):
    tasks.sort(key=lambda x: x["category"], reverse=reverse)
    print("Tasks sorted by category:" if not reverse else "Tasks sorted by category in reverse order:")
    for task in tasks:
        print(f"{task['name']} - {task['deadline']} - {task['responsible']} - {task['category']}")


def filter_tasks_by_string():
    string = input("Enter the string to filter tasks: ")
    filtered_tasks = [task for task in tasks if string in task["name"] or string in task["responsible"] or string in task["category"]]
    print(f"Tasks containing '{string}':")
    for task in filtered_tasks:
        print(f"{task['name']} - {task['deadline']} - {task['responsible']} - {task['category']}")


def show_menu():
    while True:
        print("\n---- TO-DO LIST MENU ----")
        print("1. Add category")
        print("2. Add task")
        print("3. List categories and tasks")
        print("4. Edit category")
        print("5. Edit task")
        print("6. Delete category")
        print("7. Delete task")
        print("8. Sort tasks by name")
        print("9. Sort tasks by date")
        print("10. Sort tasks by responsible person")
        print("11. Sort tasks by category")
        print("12. Filter tasks by string")
        print("0. Exit")

        option = input("\nEnter your option: ")
        if option == "1":
            add_category()
        elif option == "2":
            add_task()
        elif option == "3":
            list_categories_and_tasks()
        elif option == "4":
            edit_category()
        elif option == "5":
            edit_task()
        elif option == "6":
            delete_category()
        elif option == "7":
            delete_task()
        elif option == "8":
            sort_tasks_by_name()
        elif option == "9":
            sort_tasks_by_date()
        elif option == "10":
            sort_tasks_by_responsible()
        elif option == "11":
            sort_tasks_by_category()
        elif option == "12":
            filter_tasks_by_string()
        elif option == "0":
            print("Exiting program...")
            break
        else:
            print("Invalid option. Try again.")


if __name__ == '__main__':
    show_menu()
