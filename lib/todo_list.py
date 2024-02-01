class TodoList:
    def __init__(self):
        self.todo_list = []

    def add(self, task):
        self.todo_list.append(task)

    def incomplete(self):
        # Returns:
        #   A list of Todo instances representing the todos that are not complete
        pass

    def complete(self):
        # Returns:
        #   A list of Todo instances representing the todos that are complete
        pass

    def give_up(self):
        # Returns:
        #   Nothing
        # Side-effects:
        #   Marks all todos as complete
        pass

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
