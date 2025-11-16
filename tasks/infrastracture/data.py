import json
import os

BASE_DIR = os.path.dirname(__file__)
FILE_PATH =  os.path.join(BASE_DIR, "data.json")

print(FILE_PATH)
if not os.path.exists(FILE_PATH):
    with open(FILE_PATH, "w", encoding="utf-8") as f:
        json.dump([], f)

def load_tasks():
    with open(FILE_PATH, "r", encoding="utf-8") as f:
        return json.load(f)

def save_tasks(tasks):
    with open(FILE_PATH, "w", encoding="utf-8") as f:
        json.dump(tasks, f, ensure_ascii=False)

def add_task_record(task):
    tasks = load_tasks()
    tasks.append(task)
    save_tasks(tasks)

def delete_task_record(index):
    tasks = load_tasks()
    tasks.pop(index)
    save_tasks(tasks)

def get_tasks_records():
    return load_tasks()

def marked_task_record(index):
    tasks = load_tasks()
    tasks[index]["done"] = True
    save_tasks(tasks)