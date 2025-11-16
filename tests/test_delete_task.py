from tasks.infrastracture.data import get_tasks_records
from tasks.application.delete_task import delete_task

def test_delete_task():
    delete_task(1)
    tasks = get_tasks_records()

    assert len(tasks) == 0
