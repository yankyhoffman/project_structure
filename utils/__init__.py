# Empty __init__ file to change directory into package.

import threading

from .logger import get_project_logger

logger = get_project_logger(__name__)

program_done = threading.Event()
