from tasks.application.add_task import add_task
from tasks.infrastracture.data import get_tasks_records

def test_add_task(name):
    add_task(name)
    tasks = get_tasks_records()

    assert len(tasks) == 1
    assert tasks[0]["title"] == name
    assert tasks[0]["done"] == False