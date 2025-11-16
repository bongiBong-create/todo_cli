from tasks.application.marked_task import marked_task
from tasks.infrastracture.data import get_tasks_records

def test_marked_task():
    marked_task(1)
    tasks = get_tasks_records()

    assert tasks[0]["done"] == True