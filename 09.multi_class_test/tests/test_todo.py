from lib.todo import Todo

"""
Test that we can create an instance of the ToDo class and then access the task variable
"""

def test_initalizing_class_then_accessing_task_variable():
    todo1 = Todo("Walk the dog")
    assert todo1.task == "Walk the dog"



"""
Test that initializing the class sets the complete status to false
"""

def test_initializing_class_sets_complete_variable_to_false():
    todo1 = Todo("Walk the dog")
    assert todo1.complete == False


"""
Test that calling the mark_complete function sets that instance complete variable to true
"""

def test_mark_complete_sets_complete_status_to_true():
    todo1 = Todo("Walk the dog")
    todo1.mark_complete()
    assert todo1.complete == True
    
