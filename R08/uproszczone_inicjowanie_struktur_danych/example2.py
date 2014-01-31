class Structure:
    _fields= []
    def __init__(self, *args, **kwargs):
        if len(args) > len(self._fields):
            raise TypeError('Oczekiwano {} argumentów'.format(len(self._fields)))

		# Ustawianie wszystkich argumentów podawanych na podstawie pozycji
        for name, value in zip(self._fields, args):
            setattr(self, name, value)

        # Ustawianie pozostałych argumentów za pomocą słów kluczowych
        for name in self._fields[len(args):]:
            setattr(self, name, kwargs.pop(name))

        # Sprawdzanie, czy nie wystąpiły inne, nieznane argumenty
        if kwargs:
            raise TypeError('Nieprawidłowe argumenty: {}'.format(','.join(kwargs)))
        
# Przykład zastosowania
if __name__ == '__main__':
    class Stock(Structure):
        _fields = ['name', 'shares', 'price']

    s1 = Stock('ACME', 50, 91.1)
    s2 = Stock('ACME', 50, price=91.1)
    s3 = Stock('ACME', shares=50, price=91.1)
