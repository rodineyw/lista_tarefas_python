''' 
todo.py: A simple todo list manager
'''

import sys

# utility functions


def save(tasks):
    ''' Save tasks to file '''
    with open("tasks.txt", "w", encoding="utf-8") as file:
        for task_id, task in tasks.items():
            file.write(f"{task_id}:{task['description']}:{task['done']}\n")


def load():
    ''' Load tasks from file '''
    tasks = {}
    try:
        with open("tasks.txt", "r", encoding="utf-8") as file:
            for line in file:
                task_id, description, done = line.strip().split(":")
                tasks[int(task_id)] = {
                    "description": description, "done": done == "True"}
    except FileNotFoundError:
        pass
    return tasks


def help_task():
    ''' Print help message '''
    print("Usage:")
    print("  python todo.py add 'task description' - Add a new task")
    print("  python todo.py list - List all tasks")
    print("  python todo.py done TASK_ID - Mark a task as done")
    print("  python todo.py remove TASK_ID - Remove a task")


# tasks functions

def add(tasks, task_description):
    ''' Add a new task '''
    task_id = len(tasks) + 1
    tasks[task_id] = {"description": task_description, "done": False}
    save(tasks)
    print(f"Added task: {task_description}")


def list_task(tasks):
    ''' List all tasks '''
    for task_id, task in tasks.items():
        status = "Done" if task["done"] else "Pending"
        print(f"{task_id}: {task['description']} [{status}]")


def complete(tasks, task_id):
    ''' Mark a task as done '''
    if task_id in tasks:
        tasks[task_id]["done"] = True
        save(tasks)
        print(f"Marked task {task_id} as done")
    else:
        print(f"Task {task_id} not found")


def remove(tasks, task_id):
    ''' Remove a task '''
    if task_id in tasks:
        del tasks[task_id]
        save(tasks)
        print(f"Removed task {task_id}")
    else:
        print(f"Task {task_id} not found")


# main function
def main():
    ''' Main function '''
    tasks = load()
    if len(sys.argv) < 2:
        help()
        return

    command = sys.argv[1]

    if command == "add":
        if len(sys.argv) < 3:
            print("Error: Missing task description")
            help()
        else:
            add(tasks, sys.argv[2])
    elif command == "list":
        list(tasks)
    elif command == "done":
        if len(sys.argv) < 3:
            print("Error: Missing task ID")
            help()
        else:
            complete(tasks, int(sys.argv[2]))
    elif command == "remove":
        if len(sys.argv) < 3:
            print("Error: Missing task ID")
            help()
        else:
            remove(tasks, int(sys.argv[2]))
    else:
        print("Error: Unknown command")  # Handle unknown commands
        help()


if __name__ == "__main__":
    main()
