# Atrybuty zarządzane oparte na właściwościach

class String:
    def __init__(self, name):
        self.name = name
    def __get__(self, instance, cls):
        if instance is None:
            return self
        return instance.__dict__[self.name]

    def __set__(self, instance, value):
        if not isinstance(value, str):
            raise TypeError('Oczekiwano łańcucha znaków')
        instance.__dict__[self.name] = value


class Person:
    name = String('name')
    def __init__(self, name):
        self.name = name

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

if __name__ == '__main__':
   a = Person('Gucio')
   print(a.name)
   a.name = 'Dawid'
   print(a.name)
   try:
       a.name = 42
   except TypeError as e:
       print(e)
