Current results of execution:
```
$ python3 program.py
Before importing projects. tasks: []
Before importing projects. tasks: []
After importing projects. tasks: []
Appending process1
task: [<Task(process1)>]
Appending process2
task: [<Task(process1)>, <Task(process2)>]
After importing projects. tasks: []

```

I don't understand;
1. why is the main (`program.py`) file being executed twice, I thought that there can't be circular imports as python caches the imported modules.
2. and why is the `tasks` list empty after the processes are appended to it
