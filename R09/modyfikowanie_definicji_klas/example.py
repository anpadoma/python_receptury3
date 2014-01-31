def log_getattribute(cls):
    # Pobieranie pierwotnej implementacji
    orig_getattribute = cls.__getattribute__

    # Tworzenie nowej definicji
    def new_getattribute(self, name):
        print('Pobieranie:', name)
        return orig_getattribute(self, name)

    # Dołączanie nowej definicji do klasy i zwracanie klasy
    cls.__getattribute__ = new_getattribute
    return cls

# Przykład zastosowania
@log_getattribute
class A:
    def __init__(self,x):
        self.x = x
    def spam(self):
        pass

if __name__ == '__main__':
    a = A(42)
    print(a.x)
    a.spam()
