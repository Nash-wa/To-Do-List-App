TASKS_FILE = "tasks.txt"


def load_tasks():
    tasks = []
    try:
        with open(TASKS_FILE, "r") as f:
            for line in f:
                # each line: status|text
                status, text = line.strip().split("|", 1)
                tasks.append({"done": status == "1", "text": text})
    except FileNotFoundError:
        pass
    return tasks


def save_tasks(tasks):
    with open(TASKS_FILE, "w") as f:
        for task in tasks:
            status = "1" if task["done"] else "0"
            f.write(f"{status}|{task['text']}\n")


def show_menu():
    print("\n=== TO-DO LIST ===")
    print("1. View tasks")
    print("2. Add task")
    print("3. Mark task as done")
    print("4. Delete task")
    print("5. Exit")


def view_tasks(tasks):
    if not tasks:
        print("No tasks yet! 🎉")
        return
    for i, task in enumerate(tasks, start=1):
        status = "[x]" if task["done"] else "[ ]"
        print(f"{i}. {status} {task['text']}")


def add_task(tasks):
    text = input("Enter task: ").strip()
    if not text:
        print("Empty task ignored.")
        return
    tasks.append({"done": False, "text": text})
    print("Task added!")
def mark_task_done(tasks):
    if not tasks:
        print("No tasks to mark.")
        return
    view_tasks(tasks)
    try:
        num = int(input("Enter task number to mark as done: "))
        if 1 <= num <= len(tasks):
            tasks[num - 1]["done"] = True
            print("Task marked as done! ✅")
        else:
            print("Invalid number.")
    except ValueError:
        print("Please enter a number.")

def delete_task(tasks):
    if not tasks:
        print("No tasks to delete.")
        return
    view_tasks(tasks)
    try:
        num = int(input("Enter task number to delete: "))
        if 1 <= num <= len(tasks):
            removed = tasks.pop(num - 1)
            print(f"Deleted: {removed['text']}")
        else:
            print("Invalid number.")
    except ValueError:
        print("Please enter a number.")




