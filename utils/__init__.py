# Empty __init__ file to change directory into package.

import threading

import logsys

logger = logsys.get_project_logger(__name__)

program_done = threading.Event()
