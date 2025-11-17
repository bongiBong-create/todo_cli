from tasks.infrastracture.data import get_tasks_records
from tasks.application.delete_task import delete_task
from tests.mock_storage import path

def test_delete_task(index=1, test_path=path):
    tasks = get_tasks_records(test_path)
    length1 = len(tasks)

    delete_task(index, test_path)

    tasks = get_tasks_records(test_path)
    length2 = len(tasks)

    assert length1 != length2
