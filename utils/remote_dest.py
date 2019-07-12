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
