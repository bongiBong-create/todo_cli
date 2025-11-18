from tasks.infrastracture.storage import load_tasks
from tasks.infrastracture.storage import save_tasks
# from tasks.infrastracture.storage import load_category
# from tasks.infrastracture.storage import save_category


def add_task_record(task, path):
    tasks = load_tasks(path)
    tasks.append(task)
    save_tasks(tasks, path)

def delete_task_record(index, path):
    tasks = load_tasks(path)
    tasks.pop(index)
    save_tasks(tasks, path)

def get_tasks_records(path):
    return load_tasks(path)

def marked_task_record(index, path):
    tasks = load_tasks(path)
    tasks[index]["done"] = True
    save_tasks(tasks, path)

# def add_category(category, path):
#     categories = load_category(path)
#     categories.append(category)
#     save_category(path, categories)