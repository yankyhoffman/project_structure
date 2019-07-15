#!/usr/bin/env python

from projects import tasks
from utils import program_done

print(f"Iterating over tasks: {tasks} in {__name__}")
while True:
    for task in tasks:
        task.run()
    break # Only run once in the simulation

program_done.set()
