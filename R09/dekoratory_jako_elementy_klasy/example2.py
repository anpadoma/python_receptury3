# Przykładowa z wykorzystaniem właściwości

class Person:
    first_name = property()
    @first_name.getter
    def first_name(self):
        return self._first_name

    @first_name.setter
    def first_name(self, value):
        if not isinstance(value, str):
            raise TypeError('Oczekiwano łańcucha znaków')
        self._first_name = value

p = Person()
p.first_name = 'Dawid'
print(p.first_name)
