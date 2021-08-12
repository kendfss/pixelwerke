__all__ = 'keys values'.split()

from javascript import JSON



def keys(obj):
    obj = JSON.parse(str(obj))
    return Object.keys(obj)
def values(obj):
    obj = JSON.parse(str(obj))
    return Object.values(obj)
