import time

class _Cache:
    def __init__(self):
        self.data = None

_cache = _Cache()

def get():
    if _cache.data is None:
        _cache.data = list(_expensive_get())
    return _cache.data

def _expensive_get():
    print('Invoking expensive get')
    data = [
        'some random raw data',
        'which is in some raw format',
        'it is so raw that it will need cleaning',
        'but now it is very raw'
    ]
    for row in data:
        time.sleep(1)
        yield row
