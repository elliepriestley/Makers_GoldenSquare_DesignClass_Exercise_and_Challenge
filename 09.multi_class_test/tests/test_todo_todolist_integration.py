from lib.todo import Todo
from lib.todo_list import TodoList



"""
Test add method of TodoList adds an instance of ToDo to the public list of todos
"""

def test_that_when_adding_instance_todolist_adds_to_public_list():
    todo1 = Todo("Feed the cat")
    todo2 = Todo("Walk the dog in the morning")
    july_todos = TodoList()
    july_todos.add(todo1)
    july_todos.add(todo2)
    assert july_todos.overall_to_do_list == [todo1, todo2]


"""
Test that when adding todos to todolist, they are incomplete"""

def test_that_new_todos_added_to_todolist_are_incomplete():
    todo1 = Todo("Feed the cat")
    july_todos = TodoList()
    july_todos.add(todo1)
    assert todo1.complete == False

"""
Test that incomplete method returns list of incomplete to_do instances
"""

def test_incomplete_method_returns_list_incompleted_todos():
    todo1 = Todo("Feed the cat")
    todo2 = Todo("Walk the dog in the morning")
    july_todos = TodoList()
    july_todos.add(todo1)
    july_todos.add(todo2)
    assert july_todos.incomplete() == [todo1, todo2]

"""
test incomplete method returns empty list if there are no incomplete todos
"""

def test_incomplete_method_returns_empty_list_if_all_complete():
    todo1 = Todo("Feed the cat")
    todo2 = Todo("Walk the dog in the morning")
    july_todos = TodoList()
    july_todos.add(todo1)
    july_todos.add(todo2)
    todo1.mark_complete()
    todo2.mark_complete()
    assert july_todos.incomplete() == []


"""
Test that complete method returns list of completed todos
"""

def test_complete_method_returns_list_competed_todos():
    todo1 = Todo("Feed the cat")
    todo2 = Todo("Walk the dog in the morning")
    july_todos = TodoList()
    july_todos.add(todo1)
    july_todos.add(todo2)
    todo1.mark_complete()
    todo2.mark_complete()
    assert july_todos.complete() == [todo1, todo2]    


"""
Test that complete method returns an empty list, in the case that there are no complete todos

"""

def test_complete_method_returns_empty_list_if_all_incomplete():
    todo1 = Todo("Feed the cat")
    todo2 = Todo("Walk the dog in the morning")
    july_todos = TodoList()
    july_todos.add(todo1)
    july_todos.add(todo2)
    assert july_todos.complete() == []


"""
Test that give up method marks all todos as complete
"""

def test_give_up_method_marks_all_todos_as_complete():
    todo1 = Todo("Feed the cat")
    todo2 = Todo("Walk the dog in the morning")
    july_todos = TodoList()
    july_todos.add(todo1)
    july_todos.add(todo2)
    july_todos.give_up()
    assert todo1.complete == True
    assert todo2.complete == True
