"""
Emulate limited remote resource.
Use thread and queue to have the data sent in the backround.
"""

import time
import threading
import queue

from . import program_done
from . import logger

_q = queue.Queue()

def put(data):
    """
    Exposed remote API `put` method
    """
    logger.debug(f"putting '{data}' onto queue.")
    _q.put(data)

def _send():
    """
    Emulate remote resource,
    prints to console when data is processed.
    """
    while True:
        time.sleep(1)
        try:
            data = _q.get_nowait()
            logger.debug(f"sending '{data}' received from queue.")
            print(f"Sending '{data}'")
        except queue.Empty:
            if program_done.is_set():
                print('No more tasks')
                break

threading.Thread(target=_send).start()
