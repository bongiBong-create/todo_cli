from tasks.application.add_task import add_task
from tasks.infrastracture.data import get_tasks_records
from tests.mock_storage import path

def test_add_task(name="test", test_path=path):
    add_task(name, test_path)
    tasks = get_tasks_records(test_path)

    assert len(tasks) > 0
    assert tasks[0]["title"] == name
    assert tasks[0]["done"] == False