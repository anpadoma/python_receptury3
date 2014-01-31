# Metaklasa, która uniemożliwia stosowanie liter o różnej wielkości w identyfikatorach

class NoMixedCaseMeta(type):
    def __new__(cls, clsname, bases, clsdict):
        for name in clsdict:
            if name.lower() != name:
                raise TypeError('Błędna nazwa atrybutu: ' + name)
        return super().__new__(cls, clsname, bases, clsdict)

class Root(metaclass=NoMixedCaseMeta):
    pass

class A(Root):
    def foo_bar(self):      # Poprawnie
        pass

print('**** Przed wygenerowaniem błędu TypeError')
class B(Root):
    def fooBar(self):       # TypeError
        pass
