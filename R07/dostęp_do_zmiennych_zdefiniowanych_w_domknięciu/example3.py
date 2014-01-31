# Normalna klasa

# Przykład zastosowania
class Stack2:
    def __init__(self):
        self.items = []

    def push(self, item):
        self.items.append(item)

    def pop(self):
        return self.items.pop()

    def __len__(self):
        return len(self.items)

if __name__ == '__main__':
    import example2
    from timeit import timeit
    
    print('Używanie klasy')
    s = Stack2()
    print(timeit('s.push(1); s.pop()', 'from __main__ import s'))

    print('Używanie domknięcia')
    s = example2.Stack()
    print(timeit('s.push(1); s.pop()', 'from __main__ import s'))
