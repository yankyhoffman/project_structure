Project structure:
```
$ tree
.
├── utils
│   ├── source.py
│   ├── remote_dest.py
│   ├── local_dest.py
│   └── __init__.py
├── projects
│   ├── process2.py
│   ├── process1.py
│   └── __init__.py
└── program.py

```
Contents of libraries defined in `utils` directory:
```
$ cat utils/source.py
"""
Emulates expensive resource to get,
bringing the need to cache it for all client projects.
"""

import time

class _Cache:
    def __init__(self):
        self.data = None

_cache = _Cache()

def get():
    """
    Exposed source API for getting the data,
    get from remote resource or returns from available cache.
    """
    if _cache.data is None: # As well as cache expiration.
        _cache.data = list(_expensive_get())
    return _cache.data

def _expensive_get():
    """
    Emulate an expensive `get` request,
    prints to console if it was invoked.
    """
    print('Invoking expensive get')
    sample_data = [
        'some random raw data',
        'which is in some raw format',
        'it is so raw that it will need cleaning',
        'but now it is very raw'
    ]
    for row in sample_data:
        time.sleep(1)
        yield row

$ cat utils/remote_dest.py
"""
Emulate limited remote resource.
Use thread and queue to have the data sent in the backround.
"""

import time
import threading
import queue

_q = queue.Queue()

def put(data):
    """
    Exposed remote API `put` method
    """
    _q.put(data)

def _send(q):
    """
    Emulate remote resource,
    prints to console when data is processed.
    """
    while True:
        time.sleep(1)
        data = q.get()
        print(f"Sending {data}")

threading.Thread(target=_send, args=(_q,), daemon=True).start()

$ cat utils/local_dest.py
"""
Emulate second source of data destination.
Allowing to demonstrate need from shared libraries.
"""

import datetime
import os

# Create `out` dir if it doesn't yet exist.
_out_dir = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'out')
if not os.path.exists(_out_dir):
    os.makedirs(_out_dir)

def save(data):
    """
    Exposed API to store data locally.
    """
    out_file = os.path.join(_out_dir, 'data.txt')
    with open(out_file, 'a') as f:
        f.write(f"[{datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')}] {data}\n")

```
Main program execution script contents:
```
$ cat program.py
#!/usr/bin/env python

import os

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

```
Contents of the individual projects defined in the `projects` directory:
```
$ cat projects/process1.py
"""
Sample project that uses the shared remote resource to get data
and passes it on to another remote resource after processing.
"""

from utils.source import get
from utils.remote_dest import put
from program import register_task

@register_task(kwargs={'replace_with': 'cleaned'})
def process1(replace_with):
    raw = get()
    for record in raw:
        put(record.replace('raw', replace_with))

$ cat projects/process2.py
"""
Sample project that uses the shared remote resource to get data
and saves it locally after processing.
"""

from utils.source import get
from utils.local_dest import save
from program import register_task

@register_task()
def process2():
    raw = get()
    for record in raw:
        save(record.replace('raw', '----'))

```
Content of `__init__.py` file in the `projects` directory:
```
$ cat projects/__init__.py
"""
use __init__ file to import all projects
that might have been registered with `program.py` using `register_task`
"""

from . import process1, process2

# TODO: Dynamically import all projects (whether file or directory (as project)) that wil be created in the `projects` directory automatically (ignoring any modules that will start with an `_`)
# Something in the sense of:
# ```
# for module in os.listdir(os.path.dirname(os.path.abspath(__file__))):
#     if module.startswith('_') or module.startswith('.'):
#         continue
#     __import__(os.path.splitext(module)[0])
# ```

```
Yet when I run the program I see that;
1. `program.py` gets executed twice (once as `__main__` and once as `program`).
2. The tasks are appended (in the second execution run).
Yet when iterating over the tasks, none are found.
```
$ python3 program.py
Before importing projects as __main__. tasks: []
Before importing projects as program. tasks: []
After importing projects as program. tasks: []
Iterating over tasks: [] in program
Appending 'process1' in program
> tasks in program: [<Task(process1)>]
Appending 'process2' in program
> tasks in program: [<Task(process1)>, <Task(process2)>]
After importing projects as __main__. tasks: []
Iterating over tasks: [] in __main__

```

I don't understand;
1. Why is the main (`program.py`) file being executed twice, I thought that there can't be circular imports as python caches the imported modules?<br>
_(I took the idea of the circular imports used in flask applications, i.e. `app.py` imports `routes`, `models` etc. which all of them import `app` and use it to define the functionality, and `app.py` imports them back so that the functionality is added (as flask only runs `app.py`))_
2. Why is the `tasks` list empty after the processes are appended to it?
