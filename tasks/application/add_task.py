from tasks.infrastracture.data import add_task_record
from tasks.infrastracture.data import add_category
from tasks.infrastracture.data import get_categories

def add_task(name, category, path, category_path):
    categories = get_categories(category_path)

    if len(name) > 0:
        task = {"title": name, "category": category,"done": False}
        if category not in categories:
            add_category(category, category_path)
        add_task_record(task, path)
        print("Задачи успешно добавлена!")
    else:
        print("Дайте название задаче")