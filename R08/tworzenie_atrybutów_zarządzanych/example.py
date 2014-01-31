# Atrybuty zarządzane oparte na właściwościach

class Person:
    def __init__(self, first_name):
        self.first_name = first_name

    # Funkcja do pobierania wartości
    @property
    def first_name(self):
        return self._first_name

    # Funkcja do ustawiania wartości
    @first_name.setter
    def first_name(self, value):
        if not isinstance(value, str):
            raise TypeError('Oczekiwano łańcucha znaków')
        self._first_name = value

if __name__ == '__main__':
   a = Person('Gucio')
   print(a.first_name)
   a.first_name = 'Dawid'
   print(a.first_name)
   try:
       a.first_name = 42
   except TypeError as e:
       print(e)
