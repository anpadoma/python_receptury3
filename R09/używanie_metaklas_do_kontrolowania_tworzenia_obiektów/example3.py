# example3.py
#
# Obiekty zapisywane w pamięci podręcznej

import weakref

class Cached(type):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.__cache = weakref.WeakValueDictionary()

    def __call__(self, *args):
        if args in self.__cache:
            return self.__cache[args]
        else:
            obj = super().__call__(*args)
            self.__cache[args] = obj
            return obj
        
class Spam(metaclass=Cached):
    def __init__(self, name):
        print('Tworzenie obiektu typu Spam({!r})'.format(name))
        self.name = name

if __name__ == '__main__':
    a = Spam('foo')
    b = Spam('bar')
    print('a jest b:', a is b)
    c = Spam('foo')
    print('a jest c:', a is c)


