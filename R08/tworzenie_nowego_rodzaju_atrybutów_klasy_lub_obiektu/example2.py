# Deskryptor dla atrybutu ze sprawdzaniem typu
class Typed:
    def __init__(self, name, expected_type):
        self.name = name
        self.expected_type = expected_type

    def __get__(self, instance, cls):
        if instance is None:
            return self
        else:
            return instance.__dict__[self.name]

    def __set__(self, instance, value):
        if not isinstance(value, self.expected_type):
            raise TypeError('Oczekiwano typu ' + str(self.expected_type))
        instance.__dict__[self.name] = value

    def __delete__(self, instance):
        del instance.__dict__[self.name]

# Dekorator klasy stosujący deskryptor do wybranych atrybutów
def typeassert(**kwargs):
    def decorate(cls):
        for name, expected_type in kwargs.items():
            # Dołączanie deskryptora Typed do klasy
            setattr(cls, name, Typed(name, expected_type))
        return cls
    return decorate

# Przykład zastosowania
@typeassert(name=str, shares=int, price=float)
class Stock:
    def __init__(self, name, shares, price):
        self.name = name
        self.shares = shares
        self.price = price

if __name__ == '__main__':
    s = Stock('ACME', 100, 490.1)
    print(s.name, s.shares, s.price)
    s.shares = 50
    try:
        s.shares = 'Dużo'
    except TypeError as e:
        print(e)
