from utils.source import get
from utils.local_dest import save
from program import register_task

@register_task()
def process2():
    raw = get()
    for record in raw:
        save(record.replace('raw', '----'))
