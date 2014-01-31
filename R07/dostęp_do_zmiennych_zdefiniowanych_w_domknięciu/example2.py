# Symulowanie klas za pomocą domknięć

import sys
class ClosureInstance:
    def __init__(self, locals=None):
        if locals is None:
            locals = sys._getframe(1).f_locals

        # Aktualizowanie słownika obiektu przy użyciu jednostek wywoływalnych
        self.__dict__.update((key,value) for key, value in locals.items()
                             if callable(value) )
    # Przekierowanie metod specjalnych
    def __len__(self):
        return self.__dict__['__len__']()

# Przykład zastosowania
def Stack():
    items = []

    def push(item):
        items.append(item)

    def pop():
        return items.pop()

    def __len__():
        return len(items)

    return ClosureInstance()

if __name__ == '__main__':
    s = Stack()
    print(s)
    s.push(10)
    s.push(20)
    s.push('Witaj')
    print(len(s))
    print(s.pop())
    print(s.pop())
    print(s.pop())
