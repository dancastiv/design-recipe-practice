from lib.todo_list import *
import pytest

# if the task list is empty when user asks to show list, raise exception or return 'list is empty'
def test_show_empty_list():
    todo_list = TodoList()
    with pytest.raises(Exception) as e:
        todo_list.show_list()
    error = str(e.value)
    assert error == 'To-do list is empty. Please provide tasks.'

# # if the user adds a an item to list and then asks to show list, return list

def test_add_and_return_todo_list():
    todo_list = TodoList()
    todo_list.add('Eat breakfast')
    todo_list.add('Brush teeth')
    assert todo_list.show_list() == ['Eat breakfast', 'Brush teeth']

# # if user asks to mark task as completed, delete specified task and return new list
def test_delete_task():
    todo_list = TodoList()
    todo_list.add('Eat breakfast')
    todo_list.add('Brush teeth')
    completed = todo_list.mark_completed('Eat breakfast')
    assert completed == "Task marked as completed. Updated list: ['Brush teeth']"


# # if user tries to mark nonexistent task as completed, raise exception
def test_delete_nonexistent_task():
    todo_list = TodoList()
    todo_list.add('Eat breakfast')
    todo_list.add('Brush teeth')
    with pytest.raises(Exception) as e:
        todo_list.mark_completed('Conquer Westeros')
    error = str(e.value)
    assert error == 'Exception: Task not found. Please provide task to mark as completed.'
