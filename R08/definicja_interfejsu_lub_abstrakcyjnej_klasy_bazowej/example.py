# Definiowanie prostej abstrakcyjnej klasy bazowej

from abc import ABCMeta, abstractmethod

class IStream(metaclass=ABCMeta):
    @abstractmethod
    def read(self, maxbytes=-1):
        pass
    @abstractmethod
    def write(self, data):
        pass

# Przykładowa implementacja
class SocketStream(IStream):
    def read(self, maxbytes=-1):
        print('Odczyt')
    def write(self, data):
        print('Zapis')

# Sprawdzanie typu
def serialize(obj, stream):
    if not isinstance(stream, IStream):
        raise TypeError('Oczekiwano obiektu typu IStream')
    print('Serializowanie')

# Przykłady
if __name__ == '__main__':
    # Próba bezpośredniego utworzenia egzemplarza abstrakcyjnej klasy bazowej (nie zadziała)
    try:
        a = IStream()
    except TypeError as e:
        print(e)

    # Tworzenie egzemplarza klasy konkretnej
    a = SocketStream()
    a.read()
    a.write('Dane')

	# Przekazywanie obiektu a do funkcji ze sprawdzaniem typu
    serialize(None, a)

    # Próba przekazania obiektu podobnego do pliku do funkcji serialize (nieudana)
    import sys

    try:
        serialize(None, sys.stdout)
    except TypeError as e:
        print(e)

    # Rejestrowanie strumieni plikowych i ponowienie próby
    import io
    IStream.register(io.IOBase)

    serialize(None, sys.stdout)



