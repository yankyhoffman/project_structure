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
    logger.info(f"putting '{data}' onto queue.")
    _q.put(data)

def _send(q):
    """
    Emulate remote resource,
    prints to console when data is processed.
    """
    while True:
        time.sleep(1)
        try:
            data = q.get_nowait()
        except queue.Empty:
            if program_done.is_set():
                print('No more tasks')
                break
            continue
        logger.info(f"sending '{data}' received from queue.")
        print(f"Sending '{data}'")

threading.Thread(target=_send, args=(_q,)).start()
