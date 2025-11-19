from tasks.infrastracture.data import get_tasks_records
from shared.utils import filter_tasks
from shared.utils import print_tasks

def get_tasks(path, category):
    tasks = get_tasks_records(path)

    if len(tasks) > 0:
        if len(category) == 0 or category == "общие":
            print_tasks(tasks)
        else:
            tasks = filter_tasks(tasks, category)
            print_tasks(tasks)
    else:
        print("Список пуст, добавьте задачи")
