# Przykład z wywołaniem __new__ i związanymi z tym problemami

import weakref

class Spam:
    _spam_cache = weakref.WeakValueDictionary()
    def __new__(cls, name):
        if name in cls._spam_cache:
            return cls._spam_cache[name]
        else:
            self = super().__new__(cls)
            cls._spam_cache[name] = self
            return self

    def __init__(self, name):
        print('Inicjowanie obiektu typu Spam')
        self.name = name

if __name__ == '__main__':
    print("Informacja 'Inicjowanie obiektu typu Spam' powinna pojawić się dwukrotnie")
    s = Spam('Dawid')
    t = Spam('Dawid')
    print(s is t)

