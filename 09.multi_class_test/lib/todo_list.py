# File: lib/todo_list.py
class TodoList:
    def __init__(self):
        self.overall_to_do_list = []

    def add(self, todo):
        # Parameters:
        #   todo: an instance of Todo
        # Returns:
        #   Nothing
        # Side-effects:
        #   Adds the todo to the list of todos
        self.overall_to_do_list.append(todo)
    
    def incomplete(self):
        # Returns:
        #   A list of Todo instances representing the todos that are not complete
        incomplete = []
        for todo in self.overall_to_do_list:
            if todo.complete == False:
                incomplete.append(todo)
        return incomplete

    def complete(self):
        # Returns:
        #   A list of Todo instances representing the todos that are complete
        complete = []
        for todo in self.overall_to_do_list:
            if todo.complete == True:
                complete.append(todo)
        return complete

    def give_up(self):
        # Returns:
        #   Nothing
        # Side-effects:
        #   Marks all todos as complete
        for task in self.overall_to_do_list:
            task.mark_complete()


