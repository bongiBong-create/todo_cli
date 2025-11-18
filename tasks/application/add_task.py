from tasks.infrastracture.data import add_task_record
from tasks.infrastracture.storage import save_category


def add_task(name, category, path, category_path):
    if len(name) > 0:
        task = {"title": name, "category": category,"done": False}
        save_category(category_path, task["category"])
        add_task_record(task, path)
        print("Задачи успешно добавлена!")
    else:
        print("Дайте название задаче")