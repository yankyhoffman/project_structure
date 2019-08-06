"""
Sample project that uses the shared remote resource to get data
and passes it on to another remote resource after processing.
"""

from utils.source import get
from utils.remote_dest import put

from projects import register_task
from . import logger
from ._helper import replace_with

@register_task(kwargs={'replace_with': replace_with})
def process3(replace_with):
    raw = get()
    for record in raw:
        logger.debug(f"Processing record '{record}'")
        put(record.replace('raw', replace_with))
