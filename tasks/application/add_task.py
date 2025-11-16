from tasks.infrastracture.data import add_task_record

def add_task(name):
    if len(name) > 0:
        task = {"title": name, "done": False}
        add_task_record(task)
        print("Задачи успешно добавлена!")
    else:
        print("Дайте название задаче")