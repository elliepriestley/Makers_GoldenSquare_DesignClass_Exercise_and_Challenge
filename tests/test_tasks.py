from lib.tasks import *


def test_check_add_method_returns_string():
    task1 = Tasks()
    result1 = task1.add("Walk the dog")
    assert result1 == "The task 'Walk the dog' has been added to the task list"


def test_check_add_method_adds_to_task_list():
    task1 = Tasks()
    task1.add("Buy food shopping")
    result = task1.task_list
    assert result == ["Buy food shopping"]

def test_check_completed_method_removes_tasks():
    task1 = Tasks()
    task1.add("Feed the cat")
    task1.completed("Feed the cat")
    result = task1.task_list
    assert result == []

def test_check_completed_method_returns_string():
    task1 = Tasks()
    task1.add("Clean the kitchen")
    result = task1.completed("Clean the kitchen")
    assert result == "The task 'Clean the kitchen' has been completed and therefore removed from the task list"
    