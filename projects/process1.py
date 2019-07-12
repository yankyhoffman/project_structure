"""
Sample project that uses the shared remote resource to get data
and passes it on to another remote resource after processing.
"""

from utils.source import get
from utils.remote_dest import put
from . import register_task

@register_task(kwargs={'replace_with': 'cleaned'})
def process1(replace_with):
    raw = get()
    for record in raw:
        put(record.replace('raw', replace_with))
