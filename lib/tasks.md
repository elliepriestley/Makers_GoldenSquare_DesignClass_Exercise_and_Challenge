Single-Class Programs Design Recipe

1. Describe the Problem
Typically you will be given a short statement that does this called a user story. In industry, you may also need to ask further questions to clarify aspects of the problem.

    As a user
    So that I can keep track of my tasks
    I want a program that I can add todo tasks to and see a list of them.

    As a user
    So that I can focus on tasks to complete
    I want to mark tasks as complete and have them disappear from the list.


2. Design the Class Interface
The interface of a class includes:

-  The name of the class.
    class Tasks()

- The design of its initializer, the parameters it takes, and their data types
    init(self)

- The design of any properties the user will need to read or write, and their data types
- The design of its public methods, including:
- Their names and purposes
- What parameters they take and the data types
- What they return and that data type
- Any other side effects they might have


    class Tasks():

        __init__ method:
        Parameters: self
        Variable called task_list which is an empty list data type

        add method:
        parameters: self, task. Task is a string representing the task title to add to the task_list variable
        purpose: appends the argument task (string) to the public task_list variable as a list item.
        returns: a string indicating that the task has been added to the task_list. 

        completed method:
        parameters: self. 
        purpose: deletes the task from the self.task_list variable.
        returns: a string indicated that the task has been completed and has been removed from the task_list variable.


3. Create Examples as Tests
These are examples of the class being used with different initializer arguments, method calls, and how it should behave.

For complex challenges you might want to come up with a list of examples first and then test-drive them one by one. For simpler ones you might just dive straight into writing a test for the first example you want to address.


    Test that the add method adds new tasks:
    Given a task #add adds the task to the task_list list
    task1 = Task()
    task1.add("Walk the dog") => 
    self.task_list = ["Walk the dog]

   
    Test that the add method returns the anticipated string
    Given a task #add returns a string indicating it has been added 
    task1 = Task()
    task1.add("Walk the dog") => "The task "Walk the dog" has been added to the task list"


    Test that the completed method removes tasks:
    #completed removes the task from the task_list list:
    task1 = Task()
    task1.add("Walk the dog") => task1.task_list = ["Walk the dog"]
    task1.completed()
    self.task_list = []

     Test that the completed method returns a string:
    #completed returns a string indicating it has been removed:
    task1 = Task()
    task1.add("Walk the dog") => "The task "Walk the dog" has been added to the task list"
    task1.completed(") => "The task "walk the dog" has been completed and so is removed from the task list"


4. Implement the Behaviour
For each example you create as a test, implement the behaviour that allows the class to behave according to your example.

At this point you may wish to apply small-step test-driving to manage the complexity. This means you only write the minimum lines of the example to get the test to fail (red), then make it pass (green) and refactor, before adding another line to the test until it fails, then continue.

Then return to step 3 until you have addressed the problem you were given. You may also need to revise your design, for example if you realise you made a mistake earlier.