from lib.todo_list import *
from lib.todo import *

# check that tasks to be added to todo list have the appropriate todo class attached to them

def test_check_task_for_todo_class():
    task1 = Todo('Sleep in')
    assert isinstance(task1, Todo)

# given a todo task, adds it to list. As this is a new task, it is incomplete and thus when the incomplete list is called, task will be present

def test_return_incomplete_list():
    task1 = Todo('Eat breakfast')
    task2 = Todo('Sulk')
    todo_list = TodoList()
    todo_list.add(task1)
    todo_list.add(task2)
    assert todo_list.incomplete() == [task1, task2]

# given two todo tasks in the list with one of them marked as completed, #complete() returns the completed task in a list

def test_completed_tasks_appear_in_completed_list():
    task1 = Todo('Eat breakfast')
    task2 = Todo('Sulk')
    todo_list = TodoList()
    todo_list.add(task1)
    todo_list.add(task2)
    task1.mark_complete()
    assert todo_list.incomplete() == [task2]
    assert todo_list.complete() == [task1]

# given a list with incomplete tasks, if the user gives up on them, they are all set to complete

def test_give_up_on_tasks():
    task1 = Todo('Eat breakfast')
    task2 = Todo('Sulk')
    task3 = Todo('Red wedding my enemies')
    todo_list = TodoList()
    todo_list.add(task1)
    todo_list.add(task2)
    todo_list.add(task3)
    todo_list.give_up()
    assert todo_list.complete() == [task1, task2, task3]

# if the user has a todo list with both complete and incomplete tasks, if they give up on them and call for the complete list, all of the tasks should be there with no repeats

def test_give_up_on_final_tasks():
    task1 = Todo('Eat breakfast')
    task2 = Todo('Sulk')
    task3 = Todo('Red wedding my enemies')
    todo_list = TodoList()
    todo_list.add(task1)
    todo_list.add(task2)
    todo_list.add(task3)
    task2.mark_complete()
    todo_list.give_up()
    assert todo_list.complete() == [task1, task2, task3]