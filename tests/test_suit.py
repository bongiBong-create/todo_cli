from tests.test_add_task import test_add_task
from tests.test_delete_task import test_delete_task
from tests.test_marked_task import test_marked_task

def test_suit():
    test_add_task("test")
    test_marked_task()
    test_delete_task()

