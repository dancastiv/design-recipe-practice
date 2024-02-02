class TodoList:
    def __init__(self):
        self.todo_list = []

    def add(self, task):
        self.todo_list.append(task)

    def incomplete(self):
        incomplete_tasks = [task for task in self.todo_list if task.complete == False]
        return incomplete_tasks

    def complete(self):
        complete_tasks = [task for task in self.todo_list if task.complete == True]
        return complete_tasks

    def give_up(self):
        [task.mark_complete() for task in self.todo_list]
        self.complete()

# outdated
    def show_list(self):
        if self.todo_list == []:
            raise Exception('To-do list is empty. Please provide tasks.')
        return self.todo_list

    def mark_completed(self, task):
        if task not in self.todo_list:
            raise Exception('Exception: Task not found. Please provide task to mark as completed.')
        self.todo_list.remove(task)
        return f'Task marked as completed. Updated list: {self.todo_list}'
