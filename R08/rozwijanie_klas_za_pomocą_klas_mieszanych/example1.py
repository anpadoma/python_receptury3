class LoggedMappingMixin:
    '''
    Dodaje (w celach diagnostycznych) rejestrowanie operacji pobierania, ustawiania i usuwania wartości 
    '''
    __slots__ = ()

    def __getitem__(self, key):
        print('Pobieranie ' + str(key))
        return super().__getitem__(key)

    def __setitem__(self, key, value):
        print('Ustawianie {} = {!r}'.format(key, value))
        return super().__setitem__(key, value)

    def __delitem__(self, key):
        print('Usuwanie ' + str(key))
        return super().__delitem__(key)
    
class SetOnceMappingMixin:
    '''
    Klucz można ustawić tylko raz
    '''
    __slots__ = ()
    def __setitem__(self, key, value):
        if key in self:
            raise KeyError(str(key) + ' jest już ustawiony')
        return super().__setitem__(key, value)

class StringKeysMappingMixin:
    '''
    Wymusza stosowanie kluczy w postaci łańcuchów znaków
    '''
    __slots__ = ()
    def __setitem__(self, key, value):
        if not isinstance(key, str):
            raise TypeError('Klucz musi być łańcuchem znaków')
        return super().__setitem__(key, value)


# Przykłady

print('# ---- Przykład zastosowania klasy LoggedDict')

class LoggedDict(LoggedMappingMixin, dict):
    pass

d = LoggedDict()
d['x'] = 23
print(d['x'])
del d['x']

print('# ---- Przykład zastosowania klasy SetOnceDefaultDict')

from collections import defaultdict
class SetOnceDefaultDict(SetOnceMappingMixin, defaultdict):
    pass
 
d = SetOnceDefaultDict(list)
d['x'].append(2)
d['y'].append(3)
d['x'].append(10)
try:
    d['x'] = 23
except KeyError as e:
    print(e)

print('# ---- Przykład zastosowania klasy StringOrderedDict')
from collections import OrderedDict

class StringOrderedDict(StringKeysMappingMixin,
                        SetOnceMappingMixin,
                        OrderedDict):
    pass

d = StringOrderedDict()
d['x'] = 23
try:
    d[42] = 10
except TypeError as e:
    print(e)

try:
    d['x'] = 42
except KeyError as e:
    print(e)
