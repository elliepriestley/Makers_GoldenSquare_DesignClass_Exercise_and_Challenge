class Tasks():
    def __init__(self):
        self.task_list = []
    

    def add(self, task):
        self.task_list.append(task)
        return f"The task '{task}' has been added to the task list"

    def completed(self, task):
        self.task_list.remove(task)
        return f"The task '{task}' has been completed and therefore removed from the task list"



    
