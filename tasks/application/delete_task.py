from tasks.infrastracture.data import delete_task_record
from tasks.infrastracture.data import get_tasks_records

def delete_task(index):
    tasks = get_tasks_records()

    if 0 < index <= len(tasks):
        delete_task_record(index - 1)
        print("Задача успешна удалена!")
    else:
        print("Такой задачи не существует")