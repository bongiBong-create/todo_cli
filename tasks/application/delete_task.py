from tasks.infrastracture.data import get_tasks_records
from tasks.infrastracture.data import delete_task_record
from tasks.infrastracture.data import delete_category
from shared.utils import filter_tasks

def delete_task(index, path, category_path):
    tasks = get_tasks_records(path)

    if 0 < index <= len(tasks):
        category = tasks[index - 1]["category"]
        filtered_tasks = filter_tasks(tasks, category)
        if len(filtered_tasks) == 1:
            delete_category(category, category_path)
        delete_task_record(index - 1, path)
        print("Задача успешна удалена!")
    else:
        print("Такой задачи не существует")