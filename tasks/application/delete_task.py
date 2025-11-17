from tasks.infrastracture.data import get_tasks_records
from tasks.infrastracture.data import delete_task_record

def delete_task(index, path):
    tasks = get_tasks_records(path)

    if 0 < index <= len(tasks):
        delete_task_record(index - 1, path)
        print("Задача успешна удалена!")
    else:
        print("Такой задачи не существует")