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
