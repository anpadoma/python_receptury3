class Connection:
    def __init__(self):
        self.new_state(ClosedConnectionState)

    def new_state(self, newstate):
        self._state = newstate

    # Delegowanie do klasy ze stanem
    def read(self):
        return self._state.read(self)

    def write(self, data):
        return self._state.write(self, data)

    def open(self):
        return self._state.open(self)

    def close(self):
        return self._state.close(self)

# Klasa bazowa ConnectionState
class ConnectionState:
    @staticmethod
    def read(conn):
        raise NotImplementedError()

    @staticmethod
    def write(conn, data):
        raise NotImplementedError()

    @staticmethod
    def open(conn):
        raise NotImplementedError()

    @staticmethod
    def close(conn):
        raise NotImplementedError()

# Implementacja różnych stanów
class ClosedConnectionState(ConnectionState):
    @staticmethod
    def read(conn):
        raise RuntimeError('Nie jest otwarte')

    @staticmethod
    def write(conn, data):
        raise RuntimeError('Nie jest otwarte')

    @staticmethod
    def open(conn):
        conn.new_state(OpenConnectionState)

    @staticmethod
    def close(conn):
        raise RuntimeError('Jest już zamknięte')

class OpenConnectionState(ConnectionState):
    @staticmethod
    def read(conn):
        print('Odczyt')

    @staticmethod
    def write(conn, data):
        print('Zapis')

    @staticmethod
    def open(conn):
        raise RuntimeError('Jest już otwarte')

    @staticmethod
    def close(conn):
        conn.new_state(ClosedConnectionState)

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
