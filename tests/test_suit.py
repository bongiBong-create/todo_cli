from tests.test_add_task import test_add_task
from tests.test_delete_task import test_delete_task
from tests.test_marked_task import test_marked_task
from tests.mock_storage import path

def test_suit(test_path=path):
    test_add_task("test3", test_path)
    test_marked_task(1, test_path)
    test_delete_task(1, test_path)
