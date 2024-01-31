# {{PROBLEM}} Class Design Recipe

Copy this into a `recipe.md` in your project and fill it out.

## 1. Describe the Problem

As a user
So that I can keep track of my tasks
I want a program that I can add todo tasks to and see a list of them.

As a user
So that I can focus on tasks to complete
I want to mark tasks as complete and have them disappear from the list.

## 2. Design the Class Interface

_Include the initializer, public properties, and public methods with all parameters, return values, and side-effects._

```python
class TodoList:
    def __init__(self):
        # Side effect: initializes the list where the tasks shall go
        pass

    def add(self, task):
        # Parameters: task(string)
        # Returns nothing
        # Side effect: adds item to the list in __init__
        pass

    def show_list(self):
        # Parameters: none
        # Returns: list of tasks (list)
        pass

    def mark_completed(self, task)
        # Parameters: task to delete (string)
        # Returns: string saying 'this is the new list' and showing updated list
        pass

```

## 3. Create Examples as Tests

_Make a list of examples of how the class will behave in different situations._

``` python
# EXAMPLE

# if the task list is empty when user asks to show list, raise exception or return 'list is empty'

todo_list = TodoList()
todo_list.show_list() # => 'Task list is empty.'

# if the user adds a an item to list and then asks to show list, return list

todo_list = TodoList()
todo_list.add('Eat breakfast')
todo_list.add('Brush teeth')
todo_list.show_list()  # => ['Eat breakfast', 'Brush teeth']

# if user asks to mark task as completed, delete specified task and return new list

todo_list = TodoList()
todo_list.add('Eat breakfast')
todo_list.add('Brush teeth')
todo_list.mark_completed('Eat breakfast')  # => Task marked as completed. Updated list: ['Brush teeth']


# if user tries to mark nonexistent task as completed, raise exception

todo_list = TodoList()
todo_list.add('Eat breakfast')
todo_list.add('Brush teeth')
todo_list.mark_completed('Conquer Westeros')  # Exception: Task not found. Please provide task to mark as completed.
```

_Encode each example as a test. You can add to the above list as you go._

## 4. Implement the Behaviour

_After each test you write, follow the test-driving process of red, green, refactor to implement the behaviour._
