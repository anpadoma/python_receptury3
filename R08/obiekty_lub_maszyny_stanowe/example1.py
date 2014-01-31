class Connection:
    def __init__(self):
        self.new_state(ClosedConnection)

    def new_state(self, state):
        self.__class__ = state

    def read(self):
        raise NotImplementedError()

    def write(self, data):
        raise NotImplementedError()

    def open(self):
        raise NotImplementedError()

    def close(self):
        raise NotImplementedError()

class ClosedConnection(Connection):
    def read(self):
        raise RuntimeError('Nie jest otwarte')

    def write(self, data):
        raise RuntimeError('Nie jest otwarte')

    def open(self):
        self.new_state(OpenConnection)

    def close(self):
        raise RuntimeError('Zostało już zamknięte')

class OpenConnection(Connection):
    def read(self):
        print('Odczyt')

    def write(self, data):
        print('Zapis')

    def open(self):
        raise RuntimeError('Zostało już otwarte')

    def close(self):
        self.new_state(ClosedConnection)

# Przykład
if __name__ == '__main__':
    c = Connection()
    print(c)
    try:
        c.read()
    except RuntimeError as e:
        print(e)

    c.open()
    print(c)
    c.read()
    c.close()
    print(c)
