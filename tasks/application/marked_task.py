from tasks.infrastracture.data import marked_task_record
from tasks.infrastracture.data import get_tasks_records

def marked_task(index, path):
    tasks = get_tasks_records(path)
    if 1 <= index <= len(tasks):
        marked_task_record(index - 1, path)
        print("Задача успешна отмечена!")
    else:
        print("Такой задачи не существует")
