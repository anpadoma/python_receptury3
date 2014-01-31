# Klasa pośrednika jest tu nakładką na inny obiekt, ale
# udostępnia jego wszystkie atrybuty publiczne

class Proxy:
    def __init__(self, obj):
        self._obj = obj

    # Delegowanie wyszukiwania atrybutów do wewnętrznego obiektu
    def __getattr__(self, name):
        print('getattr:', name)
        return getattr(self._obj, name)

    # Delegowanie przypisywania wartości do atrybutów
    def __setattr__(self, name, value):
        if name.startswith('_'):
            super().__setattr__(name, value)
        else:
            print('setattr:', name, value)
            setattr(self._obj, name, value)

    # Delegowanie usuwania atrybutów
    def __delattr__(self, name):
        if name.startswith('_'):
            super().__delattr__(name)
        else:
            print('delattr:', name)
            delattr(self._obj, name)

if __name__ == '__main__':
    class Spam:
        def __init__(self, x):
            self.x = x
        def bar(self, y):
            print('Spam.bar:', self.x, y)

    # Tworzenie obiektu
    s = Spam(2)

    # Tworzenie pośrednika dla obiektu
    p = Proxy(s)

    # Korzystanie z pośrednika
    print(p.x)     # Zwraca 2
    p.bar(3)       # Zwraca "Spam.bar: 2 3"
    p.x = 37       # Ustawia s.x na 37
