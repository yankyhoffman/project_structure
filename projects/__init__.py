from . import process1, process2

# Looking for way to import all projects (whether file or directory (as project)) that wil be created in the `projects` directory automatically (ignoring any modules that will start with an `_`)
# Something in the sense of:
# ```
# for module in os.listdir(os.path.dirname(os.path.abspath(__file__))):
#     if module.startswith('_') or module.startswith('.'):
#         continue
#     __import__(os.path.splitext(module)[0])
# ```
