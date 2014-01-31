import inspect
import types

class MultiMethod:
    '''
    Reprezentuje jedną wielometodę
    '''
    def __init__(self, name):
        self._methods = {}
        self.__name__ = name

    def register(self, meth):
        '''
        Rejestrowanie nowej metody jako wielometody
        '''
        sig = inspect.signature(meth)

		# Tworzenie sygnatury na podstawie uwag metod
        types = []
        for name, parm in sig.parameters.items():
            if name == 'self': 
                continue
            if parm.annotation is inspect.Parameter.empty:
                raise TypeError(
                    'Dla argumentu {} trzeba dodać uwagę określającą typu'.format(name)
                    )
            if not isinstance(parm.annotation, type):
                raise TypeError(
                    'Uwaga dla argumentu {} musi określać typ'.format(name)
                    )
            if parm.default is not inspect.Parameter.empty:
                self._methods[tuple(types)] = meth
            types.append(parm.annotation)

        self._methods[tuple(types)] = meth

    def __call__(self, *args):
        '''
		Wywołanie metody na podstawie sygnatury z typami argumentów
        '''
        types = tuple(type(arg) for arg in args[1:])
        meth = self._methods.get(types, None)
        if meth:
            return meth(*args)
        else:
            raise TypeError('Brak metody pasującej do typów {}'.format(types))
        
    def __get__(self, instance, cls):
        '''
		Metoda deskryptora potrzebna do tego, aby wywołania działały w klasie
        '''
        if instance is not None:
            return types.MethodType(self, instance)
        else:
            return self
    
class MultiDict(dict):
    '''
    Specjalny słownik to tworzenia wielometod w metaklasie
    '''
    def __setitem__(self, key, value):
        if key in self:
			# Jeśli klucz już istnieje, dana jednostka jest wielometodą lub jednostką wywoływalną
            current_value = self[key]
            if isinstance(current_value, MultiMethod):
                current_value.register(value)
            else:
                mvalue = MultiMethod(key)
                mvalue.register(current_value)
                mvalue.register(value)
                super().__setitem__(key, mvalue)
        else:
            super().__setitem__(key, value)

class MultipleMeta(type):
    '''
    Metaklasa umożliwiająca przeciążanie metod
    '''
    def __new__(cls, clsname, bases, clsdict):
        return type.__new__(cls, clsname, bases, dict(clsdict))

    @classmethod
    def __prepare__(cls, clsname, bases):
        return MultiDict()


# Przykładowe klasy, w których zastosowano przeciążanie
class Spam(metaclass=MultipleMeta):
    def bar(self, x:int, y:int):
        print('Bar 1:', x, y)
    def bar(self, s:str, n:int = 0):
        print('Bar 2:', s, n)

# Przykład: przeciążona metoda __init__
import time
class Date(metaclass=MultipleMeta):
    def __init__(self, year: int, month:int, day:int):
        self.year = year
        self.month = month
        self.day = day

    def __init__(self):
        t = time.localtime()
        self.__init__(t.tm_year, t.tm_mon, t.tm_mday)

if __name__ == '__main__':
    s = Spam()
    s.bar(2, 3)
    s.bar('Witaj')
    s.bar('Witaj', 5)
    try:
        s.bar(2, 'Witaj')
    except TypeError as e:
        print(e)

    # Przeciążona metoda __init__
    d = Date(2012, 12, 21)
    print(d.year, d.month, d.day)
    # Pobieranie aktualnej daty
    e = Date()
    print(e.year, e.month, e.day)
