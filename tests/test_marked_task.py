from tasks.application.marked_task import marked_task
from tasks.infrastracture.data import get_tasks_records
from tests.mock_storage import path

def test_marked_task(index=1,test_path=path):
    marked_task(index, test_path)
    tasks = get_tasks_records(test_path)

    assert tasks[0]["done"] == True