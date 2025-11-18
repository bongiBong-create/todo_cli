def filter_tasks(tasks, category):
    filtred_tasks = [*filter(lambda el: el["category"] == category, tasks)]

    return filtred_tasks

def print_tasks(tasks):
    for i, task in enumerate(tasks):
        print(f"Задача №{i + 1}\n"
              f"Название: {task['title']}\n"
              f"Группа: {task["category"]}\n"
              f"Статус: {'\u2714' if task['done'] else '\u2717'}")