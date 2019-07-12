import time
import threading
import queue

_q = queue.Queue()

def put(data):
    _q.put(data)

def _send(q):
    while True:
        time.sleep(1)
        data = q.get()
        print(f"Sending {data}")

threading.Thread(target=_send, args=(_q,), daemon=True).start()
