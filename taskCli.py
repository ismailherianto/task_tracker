import json
import os
import argparse
import datetime

TASK_FILE = 'tasks.json'
nowDate = datetime.datetime.today().strftime('%Y-%m-%d %H:%M:%S')

# Load data
def load_tasks():
    if os.path.exists(TASK_FILE):
        with open(TASK_FILE, "r") as file:
            return json.load(file)
    return[]

def save_task(tasks):
    with open(TASK_FILE, "w") as file:
        json.dump(tasks, file, indent=4)

def add_task(desc):
    tasks = load_tasks()
    task = {"id": len(tasks) + 1, "description": desc, "status": "todo", "createdAt" : nowDate, "updateddAt" : ""}
    tasks.append(task)
    save_task(tasks)
    print(f"Task added successfully (ID: {task['id']})")

def list_tasks():
    tasks = load_tasks()
    if not tasks:
        print("No tasks found.")
    else:
        for task in tasks:
            if task["status"] == "in-progress" :
                status = "⏳"
            else:
                status = "✅" if task["status"] == "done" else "📝" 
            print(f"{task['id']}. {task['description']} [{status}]")



def main():
    parser = argparse.ArgumentParser(description="task-cli")
    subparsers = parser.add_subparsers(dest="command")

    add_parser = subparsers.add_parser("add", help="add new task")
    add_parser.add_argument("desc", help="task description")

    subparsers.add_parser("list", help="list all tasks")

    args = parser.parse_args()

    if args.command == 'add':
        add_task(args.desc)
    elif args.command == 'list':
        list_tasks()
    else:
        parser.print_help()


if __name__ == "__main__" :
    main()
