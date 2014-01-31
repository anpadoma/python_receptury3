class Structure:
    # Zmienna klasy określająca oczekiwane pola
    _fields= []
    def __init__(self, *args, **kwargs):
        if len(args) != len(self._fields):
            raise TypeError('Oczekiwano {} argumentów'.format(len(self._fields)))
       
        # Ustawianie argumentów
        for name, value in zip(self._fields, args):
            setattr(self, name, value)

        # Ustawianie dodatkowych argumentów (jeśli zostały podane)
        extra_args = kwargs.keys() - self._fields
        for name in extra_args:
            setattr(self, name, kwargs.pop(name))
        if kwargs:
            raise TypeError('Powtarzające się wartości argumentów {}'.format(','.join(kwargs)))
        
# Przykład zastosowania
if __name__ == '__main__':
    class Stock(Structure):
        _fields = ['name', 'shares', 'price']

    s1 = Stock('ACME', 50, 91.1)
    s2 = Stock('ACME', 50, 91.1, date='8/2/2012')
