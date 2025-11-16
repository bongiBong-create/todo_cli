from tasks.infrastracture.data import get_tasks_records

def get_tasks():
    tasks = get_tasks_records()

    if len(tasks) > 0:
        for i, task in enumerate(tasks):
            print(f"Задача №{i + 1}\n"
                  f"Название: {task['title']}\n"
                  f"Статус: {'\u2714' if task['done'] else '\u2717'}")
    else:
        print("Список пуст, добавьте задачи")