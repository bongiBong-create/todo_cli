from tasks.application.add_task import add_task
from tasks.application.delete_task import delete_task
from tasks.application.get_tasks import get_tasks
from tasks.application.marked_task import marked_task
from tasks.domain.validators import check_index
from tasks.infrastracture.storage import init_path
from tasks.infrastracture.storage import init_storage

def start_cli():
    path = init_path()
    category_path = init_path("category.json")
    init_storage(path)
    init_storage(category_path)

    commands = {
        "Добавить": "Добавить новую задачу",
        "Удалить": "Удалить задачу по номеру",
        "Отметить": "Отметить задачу как выполненную",
        "Задачи": "Показать все задачи",
        "Выход": "Выйти из приложения",}

    while True:
        command = input("Введите команду: (введите help для списка команд)\n").strip().lower()

        match command:
            case "добавить":
                name = input("Введите название задачи\n")
                category = input("Введите название группы\n").lower()
                add_task(name, category, path, category_path)
            case "удалить":
                    index = input("Введите номер задачи\n")
                    is_index = check_index(index)
                    if is_index is not None:
                        delete_task(is_index, path)
            case "задачи":
                category = input("Введите группу задач\n"
                                 "Доступные: Общие\n")
                get_tasks(path, category)
            case "отметить":
                    index = input("Введите номер задачи, которую выполнили\n")
                    is_index = check_index(index)
                    if is_index is not None:
                        marked_task(is_index, path)
            case "выход":
                break
            case "help":
                for key, value in commands.items():
                    print(f"{key} - {value}")
            case _:
                print("Введите корректную команду")