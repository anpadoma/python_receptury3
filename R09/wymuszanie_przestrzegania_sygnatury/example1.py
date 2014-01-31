# Przykładowy kod wymuszający przestrzeganie sygnatury funkcji __init__

from inspect import Signature, Parameter

def make_sig(*names):
    parms = [Parameter(name, Parameter.POSITIONAL_OR_KEYWORD)
             for name in names]
    return Signature(parms)

class Structure:
    __signature__ = make_sig()
    def __init__(self, *args, **kwargs):
        bound_values = self.__signature__.bind(*args, **kwargs)
        for name, value in bound_values.arguments.items():
            setattr(self, name, value)

# Przykład zastosowania
class Stock(Structure):
    __signature__ = make_sig('name', 'shares', 'price')

class Point(Structure):
    __signature__ = make_sig('x', 'y')

# Testy tworzenia obiektów
if __name__ == '__main__':
    s1 = Stock('ACME', 100, 490.1)
    print(s1.name, s1.shares, s1.price)

    s2 = Stock(shares=100, name='ACME', price=490.1)
    print(s2.name, s2.shares, s2.price)

    # Za mało argumentów
    try:
        s3 = Stock('ACME', 100)
    except TypeError as e:
        print(e)

    # Za dużo argumentów
    try:
        s4 = Stock('ACME', 100, 490.1, '12/21/2012')
    except TypeError as e:
        print(e)

    # Powtarzające się argumenty
    try:
        s5 = Stock('ACME', 100, name='ACME', price=490.1)
    except TypeError as e:
        print(e)

    

    
