from utils.source import get
from utils.remote_dest import put
from program import register_task

@register_task(kwargs={'replace_with': 'cleaned'})
def process1(replace_with):
    raw = get()
    for record in raw:
        put(record.replace('raw', replace_with))
