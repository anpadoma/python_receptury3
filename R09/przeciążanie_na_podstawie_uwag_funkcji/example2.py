# Inna wersja, oparta na dekoratorach

import types

class multimethod:
    def __init__(self, func):
        self._methods = {}
        self.__name__ = func.__name__
        self._default = func

    def match(self, *types):
        def register(func):
            ndefaults = len(func.__defaults__) if func.__defaults__ else 0
            for n in range(ndefaults+1):
                self._methods[types[:len(types) - n]] = func
            return self
        return register

    def __call__(self, *args):
        types = tuple(type(arg) for arg in args[1:])
        meth = self._methods.get(types, None)
        if meth:
            return meth(*args)
        else:
            return self._default(*args)
        
    def __get__(self, instance, cls):
        if instance is not None:
            return types.MethodType(self, instance)
        else:
            return self

# Przykład zastosowania
class Spam:
    @multimethod
    def bar(self, *args):
        # Jeśli nic nie pasuje, wywoływana jest metoda domyślna
        raise TypeError('Brak pasującej wersji metody bar')

    @bar.match(int, int)
    def bar(self, x, y):
        print('Bar 1:', x, y)

    @bar.match(str, int)
    def bar(self, s, n = 0):
        print('Bar 2:', s, n)

if __name__ == '__main__':
    s = Spam()
    s.bar(2, 3)
    s.bar('Witaj')
    s.bar('Witaj', 5)
    try:
        s.bar(2, 'Witaj')
    except TypeError as e:
        print(e)
