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
