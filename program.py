#!/usr/bin/env python


class Task:
    """
    Class storing `func` along with its `args` and `kwargs` to be run with.
    """
    def __init__(self, func, args=None, kwargs=None):
        self.func = func
        self.args = args if args else []
        self.kwargs = kwargs if kwargs else {}

    def run(self):
        """
        Executes stored `func` with its arguments.
        """
        self.func(*self.args, **self.kwargs)

    def __repr__(self):
        return f"<Task({self.func.__name__})>"

# List that will store the registered tasks to be executed by the main program.
tasks = []

def register_task(args=None, kwargs=None):
    """
    Registers decorated function along with the passed `args` and `kwargs` in the `tasks` list
    as a `Task` for maintained execution.
    """
    def registerer(func):
        print(f"Appending '{func.__name__}' in {__name__}")
        tasks.append(Task(func, args, kwargs)) # Saves the function as a task.
        print(f"> tasks in {__name__}: {tasks}")
        return func # returns the function untouched.
    return registerer

print(f"Before importing projects as {__name__}. tasks: {tasks}")
import projects
print(f"After importing projects as {__name__}. tasks: {tasks}")

print(f"Iterating over tasks: {tasks} in {__name__}")
while True:
    for task in tasks:
        task.run()
    break # Only run once in the simulation
