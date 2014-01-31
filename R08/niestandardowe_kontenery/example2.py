import collections

class Items(collections.MutableSequence):
    def __init__(self, initial=None):
        self._items = list(initial) if initial is None else []

    # Wymagane metody sekwencji
    def __getitem__(self, index):
        print('Pobieranie:', index)
        return self._items[index]

    def __setitem__(self, index, value):
        print('Ustawianie:', index, value)
        self._items[index] = value

    def __delitem__(self, index):
        print('Usuwanie:', index)
        del self._items[index]

    def insert(self, index, value):
        print('Wstawianie:', index, value)
        self._items.insert(index, value)

    def __len__(self):
        print('Długość')
        return len(self._items)

if __name__ == '__main__':
    a = Items([1, 2, 3])
    print(len(a))
    a.append(4)
    a.append(2)
    print(a.count(2))
    a.remove(3)
