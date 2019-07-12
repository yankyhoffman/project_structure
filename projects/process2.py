"""
Sample project that uses the shared remote resource to get data
and saves it locally after processing.
"""

from utils.source import get
from utils.local_dest import save
from . import register_task

@register_task()
def process2():
    raw = get()
    for record in raw:
        save(record.replace('raw', '----'))
