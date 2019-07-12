#!/usr/bin/env python

import os

class Task:
    def __init__(self, func, args=None, kwargs=None):
        self.func = func
        self.args = args if args else []
        self.kwargs = kwargs if kwargs else {}

    def run(self):
        self.func(*self.args, **self.kwargs)

    def __repr__(self):
        return f"<Task({self.func.__name__})>"

tasks = []

def register_task(args=None, kwargs=None):
    def registerer(func):
        print(f"Appending {func.__name__}")
        tasks.append(Task(func, args, kwargs))
        print(f"task: {tasks}")
        return func
    return registerer

print(f"Before importing projects. tasks: {tasks}")
import projects
print(f"After importing projects. tasks: {tasks}")

for task in tasks:
    task.run()
