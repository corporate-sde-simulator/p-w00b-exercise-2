import pytest
from src.taskManager import TaskManager

def test_add_task():
    tm = TaskManager()
    tm.add("Write tests")
    assert len(tm.tasks) == 1
