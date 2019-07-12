"""
Emulates expensive resource to get,
bringing the need to cache it for all client projects.
"""

import time

class _Cache:
    def __init__(self):
        self.data = None

_cache = _Cache()

def get():
    """
    Exposed source API for getting the data,
    get from remote resource or returns from available cache.
    """
    if _cache.data is None: # As well as cache expiration.
        _cache.data = list(_expensive_get())
    return _cache.data

def _expensive_get():
    """
    Emulate an expensive `get` request,
    prints to console if it was invoked.
    """
    print('Invoking expensive get')
    sample_data = [
        'some random raw data',
        'which is in some raw format',
        'it is so raw that it will need cleaning',
        'but now it is very raw'
    ]
    for row in sample_data:
        time.sleep(1)
        yield row
