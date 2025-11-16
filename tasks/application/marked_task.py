from tasks.infrastracture.data import marked_task_record
from tasks.infrastracture.data import get_tasks_records

def marked_task(index):
    tasks = get_tasks_records()
    if 1 <= index <= len(tasks):
        marked_task_record(index - 1)
        print("Задача успешна отмечена!")
    else:
        print("Такой задачи не существует")
