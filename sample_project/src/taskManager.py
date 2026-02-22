"""
Task Manager CLI — manages a list of tasks with priorities.
Author: Practice project for Exercise 2
"""

class Task:
    def __init__(self, title, priority='medium'):
        self.title = title
        self.priority = priority
        self.done = False

    def complete(self):
        self.done = True

class TaskManager:
    def __init__(self):
        self.tasks = []

    def add(self, title, priority='medium'):
        # BUG: Doesn't check for duplicate titles
        self.tasks.append(Task(title, priority))

    def complete(self, title):
        for task in self.tasks:
            if task.title == title:
                task.complete()
                return True
        return False

    def list_pending(self):
        return [t for t in self.tasks if not t.done]
