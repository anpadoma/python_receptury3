# Atrybuty zarządzane oparte na właściwościach

class Person:
    def __init__(self, name):
        self.name = name

    # Funkcja do pobierania wartości
    @property
    def name(self):
        return self._name

    # Funkcja do ustawiania wartości
    @name.setter
    def name(self, value):
        if not isinstance(value, str):
            raise TypeError('Oczekiwano łańcucha znaków')
        self._name = value

    @name.deleter
    def name(self):
        raise AttributeError("Nie można usunąć atrybutu")

class SubPerson(Person):
    @property
    def name(self):
        print('Pobieranie imienia')
        return super().name

    @name.setter
    def name(self, value):
        print('Ustawianie imienia na:', value)
        super(SubPerson, SubPerson).name.__set__(self, value)

    @name.deleter
    def name(self):
        print('Usuwanie imienia')
        super(SubPerson, SubPerson).name.__delete__(self)

class SubPerson2(Person):
    @Person.name.setter
    def name(self, value):
        print('Ustawianie imienia na:', value)
        super(SubPerson2, SubPerson2).name.__set__(self, value)

class SubPerson3(Person):
    #@property
    @Person.name.getter
    def name(self):
        print('Pobieranie imienia')
        return super().name

if __name__ == '__main__':
   a = Person('Gucio')
   print(a.name)
   a.name = 'Dawid'
   print(a.name)
   try:
       a.name = 42
   except TypeError as e:
       print(e)
