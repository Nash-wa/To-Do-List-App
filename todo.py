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

def main():
    tasks = load_tasks()

    while True:
        show_menu()
        choice = input("Choose an option (1-5): ").strip()

        if choice == "1":
            view_tasks(tasks)
        elif choice == "2":
            add_task(tasks)
            save_tasks(tasks)
        elif choice == "3":
            # Person B will implement this function
            mark_task_done(tasks)
            save_tasks(tasks)
        elif choice == "4":
            # Person B will implement this function
            delete_task(tasks)
            save_tasks(tasks)
        elif choice == "5":
            save_tasks(tasks)
            print("Goodbye! 👋")
            break
        else:
            print("Invalid choice, try again.")


if __name__ == "__main__":
    main()
