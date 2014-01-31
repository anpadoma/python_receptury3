# Prosty przykład

class Spam:
    def __init__(self, name):
        self.name = name

# Obsługa zapisywania w pamięci podręcznej
import weakref
_spam_cache = weakref.WeakValueDictionary()

def get_spam(name):
    if name not in _spam_cache:
        s = Spam(name)
        _spam_cache[name] = s
    else:
        s = _spam_cache[name]
    return s

if __name__ == '__main__':
    a = get_spam('foo')
    b = get_spam('bar')
    print('a jest b:', a is b)
    c = get_spam('foo')
    print('a jest c:', a is c)


