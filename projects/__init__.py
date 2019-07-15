"""
use __init__ file to import all projects
that might have been registered with `program.py` using `register_task`
"""

class _Task:
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
        tasks.append(_Task(func, args, kwargs)) # Saves the function as a task.
        return func # returns the function untouched.
    return registerer

from . import process1, process2

# TODO: Dynamically import all projects (whether file or directory (as project)) that wil be created in the `projects` directory automatically (ignoring any modules that will start with an `_`)
# Something in the sense of:
# ```
# for module in os.listdir(os.path.dirname(os.path.abspath(__file__))):
#     if module.startswith('_') or module.startswith('.'):
#         continue
#     __import__(os.path.splitext(module)[0])
# ```
