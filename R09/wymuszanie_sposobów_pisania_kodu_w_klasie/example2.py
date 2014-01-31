# Używanie metaklasy do generowania ostrzeżeń dotyczących błędnej sygnatury

from inspect import signature
import logging

class MatchSignaturesMeta(type):
    def __init__(self, clsname, bases, clsdict):
        super().__init__(clsname, bases, clsdict)
        sup = super(self, self)
        for name, value in clsdict.items():
            if name.startswith('_') or not callable(value):
                continue
			# Pobranie poprzedniej definicji (jeśli istnieje) i porównanie sygnatur
            prev_dfn = getattr(sup,name,None)
            if prev_dfn:
                prev_sig = signature(prev_dfn)
                val_sig = signature(value)
                if prev_sig != val_sig:
                    logging.warning('Niedopasowana sygnatura w %s. %s != %s',
                                value.__qualname__, str(prev_sig), str(val_sig))

# Przykład
class Root(metaclass=MatchSignaturesMeta):
    pass

class A(Root):
    def foo(self, x, y):
        pass

    def spam(self, x, *, z):
        pass

# Klasa z nowymi definicjami metod z nieco zmodyfikowanymi sygnaturami
class B(A):
    def foo(self, a, b):
        pass

    def spam(self,x,z):
        pass
